# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .items import HouseSaleModel,HouseSaleVisitModel,HouseMappingModel,database_proxy
from peewee import *
import ast
import logging
from datetime import datetime
import time
# peewee数据库操作

class LianjiaCrawlerPipeline(object):
    def __init__(self,mysql_setting):
        super(LianjiaCrawlerPipeline, self).__init__()
        self.max_in_num = 100;
        self._insale_items = [] # 插入房源的数据
        self._invisit_items = [] # 插入房源访问的数据
        self.mysql_setting = mysql_setting


    @classmethod
    def from_settings(cls, settings):
        return cls(
            mysql_setting=settings['MYSQL_SETTING']
        )

    #打开spider
    def open_spider(self, spider):
        mysql_settings = ast.literal_eval(self.mysql_setting)
        MYSQL_HOST = mysql_settings[spider.city_id]['MYSQL_HOST']
        MYSQL_DBNAME = mysql_settings[spider.city_id]['MYSQL_DBNAME']
        MYSQL_USER = mysql_settings[spider.city_id]['MYSQL_USER']
        MYSQL_PASSWORD = mysql_settings[spider.city_id]['MYSQL_PASSWORD']
        MYSQL_PORT = mysql_settings[spider.city_id]['MYSQL_PORT']
        self.db = MySQLDatabase(MYSQL_DBNAME,host=MYSQL_HOST,port=MYSQL_PORT,user=MYSQL_USER, passwd=MYSQL_PASSWORD, charset='utf8')
        database_proxy.initialize(self.db)
        self.db.connect(reuse_if_open=True)


    def process_item(self, item, spider):
        if HouseSaleModel.table_exists() == False:
            HouseSaleModel.create_table() # 创建表
        if HouseSaleVisitModel.table_exists() == False:
            HouseSaleVisitModel.create_table()
        if HouseMappingModel.table_exists() == False:
            HouseMappingModel.create_table()

        try:
            if item['item_type'] == 'house_sale_visit':#带看数据，查看数据是否存在，存在插入新的数量，不存在，插入当前数量
                item.pop('item_type')
                visit_sum = 0
                result = HouseSaleVisitModel.select(fn.SUM(HouseSaleVisitModel.visit_num).alias('visit_sum')).where(HouseSaleVisitModel.net_id==item['net_id'],
                                                                                                                             HouseSaleVisitModel.sale_order_no==item['sale_order_no'],
                                                                                                                             HouseSaleVisitModel.visit_economic_id==item['visit_economic_id'])
                if result.dicts()[0].get('visit_sum'):
                    visit_sum = result.dicts()[0].get('visit_sum')
                if visit_sum and visit_sum != item['visit_num']:
                    item['visit_num'] = item['visit_num']-visit_sum
                self._invisit_items.append(item)
                # 执行插入
                if len(self._invisit_items) == self.max_in_num:
                    self.inser_to_visitsql()
            else:
                item.pop('item_type')
                self._insale_items.append(item)
                if len(self._insale_items) == self.max_in_num:
                    self.insert_to_salesql()

        except Exception as e:
            logging.warning('Error',e)
        return item

    #批量插入数据
    def insert_to_salesql(self):
        # 添加日期
        times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time_array = time.strptime(times, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(time_array))
        if self._insale_items:
            with self.db.atomic():
                HouseSaleModel.insert_many(self._insale_items). \
                    on_conflict(update={HouseSaleModel.edit_time: time_stamp,HouseSaleModel.is_deal:0,HouseSaleModel.xj_date:None,HouseSaleModel.xj_year:0,HouseSaleModel.xj_month:0}).execute()
                logging.warning('执行房源数据成功。')
                del self._insale_items[:]

    def inser_to_visitsql(self):
        if self._invisit_items:
            with self.db.atomic():
                HouseSaleVisitModel.insert_many(self._invisit_items).on_conflict_ignore().execute()
                logging.warning('执行带看数据成功。')
                del self._invisit_items[:]


    #关闭的时候调用剩下的数据
    def close_spider(self, spider):
        self.insert_to_salesql()
        self.inser_to_visitsql()
        self.db.close()