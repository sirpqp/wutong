# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WutongInternationalCompanyItem(scrapy.Item):
    """公司信息"""
    name = scrapy.Field() # 名字
    thumbs = scrapy.Field()  # 形象展示 图片地址 不多于4张 地址间以空格分隔
    introduce = scrapy.Field()  # 简介
    truename = scrapy.Field()  # 联系人
    mobile = scrapy.Field()  # 手机
    tel = scrapy.Field()  # 联系电话
    area = scrapy.Field()  # 总部所在地 ex: 山东省 济南市 市辖区
    address = scrapy.Field()  # 总部地址（详细）
    business_license = scrapy.Field()  # 营业执照
    representative = scrapy.Field()  # 法人代表/负责人
    established = scrapy.Field()  # 成立时间
    wxt = scrapy.Field()  # 物信通 年数 ex: 2
    honor = scrapy.Field()  # 荣誉称号 先锋/标杆/领军企业... 等级 (v2..) ex: 先锋V2
    link = scrapy.Field()  # 物通网地址


class WutongInternationalCarriageItem(scrapy.Item):
    """承运信息：整箱运价，拼箱运价，散杂运价，空运运价，公路运价，铁路运价"""
    name = scrapy.Field()  # 公司名字
    company_url = scrapy.Field()  # 公司介绍链接
    carriage_type = scrapy.Field()  # 承运类型
    starting = scrapy.Field()  # 出发地
    arrive = scrapy.Field()  # 目的地
    price = scrapy.Field()  # 运价 json格式
    meta = scrapy.Field()  # 承运详情 ：承运人，航空公司，航班周期，运抵时间，是否中专，付款方式等等 json格式
    contact_person = scrapy.Field()  # 联系人
    mobile = scrapy.Field()  # 手机
    tel = scrapy.Field()  # 电话
    QQ = scrapy.Field()  # QQ
    remark = scrapy.Field()  # 备注说明


