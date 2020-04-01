# -*- coding: utf-8 -*-
import re
import json

import scrapy
from start import crawl

from parse_file.parse_totall import get_price, get_meta
from items import WutongInternationalCarriageItem


class WutonginternationalSpider(scrapy.Spider):
    name = 'wutonginternational'
    allowed_domains = ['inter.chinawutong.com', 'm.chinawutong.com']
    start_urls = ['http://inter.chinawutong.com/%s']
    carriage_type_list = ['fcl/', 'lcl/', 'bulk/', 'air/', 'land/', 'rail/']

    # carriage_type_list = ['rail/']

    def start_requests(self):
        # 承运类型：整箱，拼箱，散杂，空运，铁路，公路
        for carriage_type in self.carriage_type_list:
            url = self.start_urls[0] % carriage_type
            headers = {
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cookie': 'ASP.NET_SessionId=bmy1bhqdxpo2ic3n4piujpy5'
            }
            if carriage_type == 'fcl/' or carriage_type == 'air/':
                yield scrapy.Request(
                    url=url,
                    headers=headers,
                    callback=self.parse_line_list,
                    meta={
                        'carriage_type': carriage_type
                    }
                )
            else:
                yield scrapy.Request(
                    url=url,
                    headers=headers,
                    callback=self.parse_line_detail,
                    meta={
                        'carriage_type': carriage_type
                    }
                )

    def parse_line_list(self, response):
        fcl_headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://inter.chinawutong.com/fcl/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        a_list = response.xpath('//div[@class="juHeList"]//a')
        for a in a_list:
            fcl_url = a.xpath('./@href').extract_first()
            yield scrapy.Request(
                url=fcl_url,
                callback=self.parse_line_detail,
                headers=fcl_headers,
                meta={
                    'carriage_type': response.meta['carriage_type']
                }
            )

    def parse_line_detail(self, response):
        # 获取线路详情

        ul_list = response.xpath('//ul[@class="neiRong"]')
        for ul in ul_list:
            detail_url = ul.xpath('//a[@class="qyd"]/@href').extract_first(default='')
            company_name = ul.xpath('//a[@class="gongSi"]/text()').extract_first(default='').strip()
            for carriage_type in self.carriage_type_list:
                if carriage_type in response.url:
                    url = detail_url.replace('inter', 'm').replace(carriage_type, 'inter/%s' % carriage_type)

            yield scrapy.Request(
                # 详情页面，需要替用移动端访问
                url=url,
                callback=self.parse_detail,
                headers={
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Mobile Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'Referer': 'http://inter.chinawutong.com/lcl/65538.html',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                },
                meta={
                    'carriage_type': response.meta['carriage_type'],
                    'name': company_name,
                }
            )

        # 下一页
        check_next = response.xpath('//ul[@class="subPaging"][contains(string(),"下一页")]')
        if check_next:
            next_li = check_next.xpath('./li')[2:-3]
            for li in next_li:
                next_url = li.xpath('./a/@href').extract_first()
                print(next_url)
                yield scrapy.Request(
                    url=next_url,
                    callback=self.parse_line_detail,
                    meta={
                        'carriage_type': response.meta['carriage_type']
                    }
                )

    def parse_detail(self, response):
        result = re.search(r'<p>(.*?)<span class="jianTou"></span>(.*?)</p>', response.text)
        if result:
            starting = result.group(1)
            arrive = result.group(2)
        else:
            starting = None
            arrive = None

        # 运价
        price = get_price(response)

        # 其余字段组成meta = {}
        meta = get_meta(response)

        # 联系人
        contact_person = response.xpath(
            'string(//span[@class="col999" and text()="联系人："]/following-sibling::span)').extract_first()

        # 手机
        mobile = response.xpath(
            'string(//span[@class="col999" and text()="手机： "]/following-sibling::span)').extract_first()

        # 电话
        tel = response.xpath('string(//span[@class="col999" and text()="电话："]/following-sibling::span)').extract_first()

        # QQ
        QQ = response.xpath('string(//span[@class="col999" and text()="QQ： "]/following-sibling::span)').extract_first()

        # 说明备注
        remark = response.xpath(
            'string(//span[@class="col999" and text()="说明备注："]/following-sibling::span)').extract_first().strip()

        # 公司详情链接
        company_a = response.xpath('//a[@class="neiRong w70"]/@href').extract_first()
        company_url = 'http://%s.chinawutong.com/' % company_a.split("/")[-2]
        item = WutongInternationalCarriageItem()
        item['company_url'] = company_url
        item['starting'] = starting
        item['arrive'] = arrive
        item['name'] = response.meta['name']
        item['price'] = price if isinstance(price, str) else json.dumps(price, ensure_ascii=False)
        item['meta'] = meta if isinstance(meta, str) else json.dumps(meta, ensure_ascii=False)
        item['contact_person'] = contact_person
        item['mobile'] = mobile
        item['tel'] = tel
        item['QQ'] = QQ
        item['remark'] = remark
        if response.meta['carriage_type'] == 'fcl/':
            item['carriage_type'] = '整箱'
        elif response.meta['carriage_type'] == 'lcl/':
            item['carriage_type'] = '拼箱'
        elif response.meta['carriage_type'] == 'bulk/':
            item['carriage_type'] = '散杂'
        elif response.meta['carriage_type'] == 'air/':
            item['carriage_type'] = '空运'
        elif response.meta['carriage_type'] == 'land/':
            item['carriage_type'] = '公路'
        elif response.meta['carriage_type'] == 'rail/':
            item['carriage_type'] = '铁路'

        print(item)


if __name__ == '__main__':
    crawl(WutonginternationalSpider)
