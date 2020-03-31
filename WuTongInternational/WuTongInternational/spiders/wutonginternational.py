# -*- coding: utf-8 -*-
import scrapy
from start import crawl


class WutonginternationalSpider(scrapy.Spider):
    name = 'wutonginternational'
    allowed_domains = ['inter.chinawutong.com']
    start_urls = ['http://inter.chinawutong.com/%s']
    carriage_type_list = ['fcl/', 'lcl/', 'bulk/', 'air/', 'land/', 'rail/']

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

            yield scrapy.Request(
                url=url,
                headers=headers,
                callback=self.parse,
            )

    def parse(self, response):
        # 整箱
        if 'fcl/' in response.url:
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
                    callback=self.parse_fcl,
                    headers=fcl_headers,
                )

        # 拼箱
        if 'lcl/' in response.url:
            pass

        # 散杂
        if 'bulk/' in response.url:
            pass

        # 空运
        if 'air/' in response.url:
            pass

        # 公路
        if 'land/' in response.url:
            pass

        # 铁路
        if 'rail/' in response.url:
            pass

    def parse_fcl(self, response):
        pass


if __name__ == '__main__':
    crawl(WutonginternationalSpider)
