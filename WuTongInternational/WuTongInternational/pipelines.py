# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from DB.mysql import MySqlClient, MysqlDbPool
from parsetools.db import get_query_args_by_item


class WutonginternationalPipeline(object):
    def __init__(self):
        self.mysql = MySqlClient()

    def process_item(self, item, spider):

        query, args = get_query_args_by_item(item, 'wutong_inter_line')

        self.mysql.execute(query, args)

        return item

    def close_spider(self, spider):
        self.mysql.close()
