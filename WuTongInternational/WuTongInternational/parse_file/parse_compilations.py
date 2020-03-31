

def parse_netpoints(response):

    tags = {
        'point_name': None,
        'point_address': None,
        'tel': None,
        'mobile': None
    }
    # response = HtmlResponse(response.url, body=response.text, encoding='gbk')
    netpoints_info = {}
    th_list = response.xpath('//div[@class="wdmain"]/table/thead//th')
    for ind, th in enumerate(th_list):
        if '网点' in th.xpath('string(.)').extract_first().strip():
            tags['point_name'] = ind
        elif '地址' in th.xpath('string(.)').extract_first().strip():
            tags['point_address'] = ind
        elif '电话' in th.xpath('string(.)').extract_first().strip():
            tags['tel'] = ind
        elif '手机' in th.xpath('string(.)').extract_first().strip():
            tags['mobile'] = ind

    tr_list = response.xpath('//div[@class="wdmain"]/table/tbody//tr')
    for tr in tr_list:
        td_list = tr.xpath('.//td')
        for idx, td in enumerate(td_list):
            if tags['point_name'] == idx:
                netpoints_info['point_name'] = td.xpath('string(.)').extract_first()
            elif tags['point_address'] == idx:
                netpoints_info['point_address'] = td.xpath('string(.)').extract_first()
            elif tags['tel'] == idx:
                netpoints_info['phone'] = td.xpath('string(.)').extract_first()
            elif tags['mobile'] == idx:
                netpoints_info['phone'] += ';' + td.xpath('string(.)').extract_first()
    if '*' not in netpoints_info['phone'] and netpoints_info['phone'] != ';\t':
        yield netpoints_info
