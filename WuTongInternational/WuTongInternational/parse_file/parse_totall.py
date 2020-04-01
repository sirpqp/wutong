import re
import json

from lxml import etree


def get_price(response):
    if 'fcl' in response.url:
        fcl_price = get_fcl_air_price(response)
        return json.dumps(fcl_price, ensure_ascii=False)
    if 'lcl' in response.url:
        return response.xpath('string(//span[@class="col999" and text()="运价： "]/following-sibling::span)').extract_first()
    if 'bulk' in response.url:
        return response.xpath('string(//span[@class="col999" and text()="运价： "]/following-sibling::span)').extract_first()
    if 'air' in response.url:
        air_price = get_fcl_air_price(response)
        return json.dumps(air_price, ensure_ascii=False)
    if 'land' in response.url:
        land_price = get_land_price(response)
        return json.dumps(land_price, ensure_ascii=False)
    if 'rail' in response.url:
        return response.xpath('string(//span[@class="col999" and text()=" 运价："]/following-sibling::span)').extract_first()


def get_meta(response):
    meta = {}
    if 'fcl' in response.url:
        # 承运人
        carrier = response.xpath(
            'string(//span[@class="col999" and text()="承运人： "]/following-sibling::span)').extract_first()
        # 航程
        voyages = response.xpath(
            'string(//span[@class="col999" and text()="航程："]/following-sibling::span)').extract_first()
        # 箱型
        box = response.xpath(
            'string(//span[@class="col999" and text()="箱型： "]/following-sibling::span)').extract_first()
        # 中转港
        reshipment_port = response.xpath(
            'string(//span[@class="col999" and text()="中转港："]/following-sibling::span)').extract_first()
        # 离港班期
        departure_schedule = response.xpath(
            'string(//span[@class="col999" and text()="离港班期："]/following-sibling::span)').extract_first()
        # 提单要求
        bill_of_lading_requirements = response.xpath(
            'string(//span[@class="col999" and text()="提单要求："]/following-sibling::span)').extract_first()
        # 付款方式
        payment_method = response.xpath(
            'string(//span[@class="col999" and (text()="付款方式：" or text()="付款方式： ")]/following-sibling::span)').extract_first()
        
        meta['carrier'] = carrier
        meta['box'] = box
        meta['transshipment_port'] = reshipment_port
        meta['voyages'] = voyages
        meta['departure_schedule'] = departure_schedule
        meta['bill_of_lading_requirements'] = bill_of_lading_requirements
        meta['payment_method'] = payment_method

    if 'lcl' in response.url:
        # 承运人
        carrier = response.xpath(
            'string(//span[@class="col999" and text()="承运人： "]/following-sibling::span)').extract_first()
        # 箱型
        box = response.xpath(
            'string(//span[@class="col999" and text()="箱型： "]/following-sibling::span)').extract_first()
        # 中转港
        reshipment_port = response.xpath(
            'string(//span[@class="col999" and text()="中转港："]/following-sibling::span)').extract_first()
        # 航程
        voyages = response.xpath(
            'string(//span[@class="col999" and text()="航程："]/following-sibling::span)').extract_first()
        # 离港班期
        departure_schedule = response.xpath(
            'string(//span[@class="col999" and text()="离港班期："]/following-sibling::span)').extract_first()
        # 提单要求
        bill_of_lading_requirements = response.xpath(
            'string(//span[@class="col999" and text()="提单要求："]/following-sibling::span)').extract_first()
        # 付款方式
        payment_method = response.xpath(
            'string(//span[@class="col999" and (text()="付款方式：" or text()="付款方式： ")]/following-sibling::span)').extract_first()
        
        meta['carrier'] = carrier
        meta['box'] = box
        meta['transshipment_port'] = reshipment_port
        meta['voyages'] = voyages
        meta['departure_schedule'] = departure_schedule
        meta['bill_of_lading_requirements'] = bill_of_lading_requirements
        meta['payment_method'] = payment_method

    if 'bulk' in response.url:
        # 运载方式
        transportation = response.xpath(
            'string(//span[@class="col999" and text()="运载方式： "]/following-sibling::span)').extract_first()
        # 接载类型
        cargo_type = response.xpath(
            'string(//span[@class="col999" and text()="接载类型："]/following-sibling::span)').extract_first()
        # 船舶类型
        ship_types = response.xpath(
            'string(//span[@class="col999" and text()=" 船舶类型："]/following-sibling::span)').extract_first()

        meta['transportation'] = transportation
        meta['jiezai'] = cargo_type
        meta['ship_types'] = ship_types

    if 'air' in response.url:
        # 航空公司
        airline = response.xpath(
            'string(//span[@class="col999" and text()="航空公司： "]/following-sibling::span)').extract_first()
        # 运抵时间
        voyages = response.xpath(
            'string(//span[@class="col999" and text()="运抵时间："]/following-sibling::span)').extract_first()
        # 航班周期
        departure_schedule = response.xpath(
            'string(//span[@class="col999" and text()="航班周期： "]/following-sibling::span)').extract_first()
        # 是否中转
        is_reshipment = response.xpath(
            'string(//span[@class="col999" and text()="是否中转："]/following-sibling::span)').extract_first()
        # 付款方式
        payment_method = response.xpath(
            'string(//span[@class="col999" and (text()="付款方式：" or text()="付款方式： ")]/following-sibling::span)').extract_first()
        
        meta['payment_method'] = payment_method
        meta['airline'] = airline
        meta['voyages'] = voyages
        meta['is_reshipment'] = is_reshipment
        meta['departure_schedule'] = departure_schedule

    if 'land' in response.url:
        # 运输方式
        mode_of_transport = response.xpath(
            'string(//span[@class="col999" and text()=" 运输方式： "]/following-sibling::span)').extract_first()
        # 车辆类型
        vehicle_type = response.xpath(
            'string(//span[@class="col999" and text()="车辆类型： "]/following-sibling::span)').extract_first()
        # 车长
        vehicle_length = response.xpath(
            'string(//span[@class="col999" and text()="车长： "]/following-sibling::span)').extract_first().strip()
        
        meta['mode_of_transport'] = mode_of_transport
        meta['vehicle_type'] = vehicle_type
        meta['vehicle_length'] = vehicle_length

    if 'rail' in response.url:
        # 途径地
        stopover = response.xpath(
            'string(//span[@class="col999" and text()=" 途径地： "]/following-sibling::span)').extract_first()
        # 运输方式
        mode_of_transport = response.xpath(
            'string(//span[@class="col999" and text()=" 运输方式： "]/following-sibling::span)').extract_first()
        # 车皮类型
        chepi_type = response.xpath(
            'string(//span[@class="col999" and text()="车皮类型： "]/following-sibling::span)').extract_first()
        # 载重
        carrying_capacity = response.xpath(
            'string(//span[@class="col999" and text()=" 载重："]/following-sibling::span)').extract_first()
        # 体积
        bulk = response.xpath("string(//li[contains(string(),'体积')])").extract_first().split('：')[-1]
        # 付款方式
        payment_method = response.xpath(
            'string(//span[@class="col999" and (text()="付款方式：" or text()="付款方式： ")]/following-sibling::span)').extract_first()
        
        meta['stopover'] = stopover
        meta['mode_of_transport'] = mode_of_transport
        meta['chepi_type'] = chepi_type
        meta['carrying_capacity'] = carrying_capacity
        meta['bulk'] = bulk
        meta['payment_method'] = payment_method

    return json.dumps(meta, ensure_ascii=False)


def get_fcl_air_price(response):
    box_dict = dict()
    price_dict = dict()
    if 'air' in response.url:
        price_ul = response.xpath('//div[@class="list"]/ul')
    else:
        price_ul = response.xpath('//div[@class="list zheng"]/ul')
    for idx, li in enumerate(price_ul[0].xpath("./li")):
        box_dict[li.xpath('./text()').extract_first()] = idx
    if 'air' in response.url:
        for idx, li in enumerate(price_ul[1].xpath("./li")):
            if idx == box_dict['Min']:
                price_dict['Min'] = li.xpath('./text()').extract_first()
            elif idx == box_dict['+45']:
                price_dict['+45'] = li.xpath('./text()').extract_first()
            elif idx == box_dict['+100 ']:
                price_dict['+100 '] = li.xpath('./text()').extract_first()
            elif idx == box_dict['+300']:
                price_dict['+300'] = li.xpath('./text()').extract_first()
            elif idx == box_dict['+500']:
                price_dict['+500'] = li.xpath('./text()').extract_first()
            elif idx == box_dict['+1000']:
                price_dict['+1000'] = li.xpath('./text()').extract_first()
    else:
        for idx, li in enumerate(price_ul[1].xpath("./li")):
            if idx == box_dict['20′']:
                price_dict['20′'] = li.xpath('./text()').extract_first()
            elif idx == box_dict['40′']:
                price_dict['40′'] = li.xpath('./text()').extract_first()
            elif idx == box_dict['40HQ']:
                price_dict['40HQ'] = li.xpath('./text()').extract_first()
            elif idx == box_dict['45′']:
                price_dict['45′'] = li.xpath('./text()').extract_first()

    return price_dict


def get_land_price(response):
    price_dict = dict()
    # 重货价
    heavy_cost = response.xpath(
            'string(//span[@class="col999" and text()=" 重货价："]/following-sibling::span)').extract_first()
    # 轻货价
    light_cost = response.xpath(
            'string(//span[@class="col999" and text()=" 轻货价："]/following-sibling::span)').extract_first()
    price_dict['heavy_cost'] = heavy_cost
    price_dict['light_cost'] = light_cost

    return price_dict

