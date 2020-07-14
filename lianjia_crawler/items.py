# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from peewee import *

#db = MySQLDatabase("hw_data_sh",host='114.80.118.231',port=3306,user='root', passwd='231!@#qwe', charset='utf8')

database_proxy = DatabaseProxy()

class BaseModel(Model):
    class Meta:
        database = database_proxy # This model uses the "people.db" database.

class LianjiaCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 楼盘匹配表
class HouseMappingModel(BaseModel):
    net_id = SmallIntegerField(verbose_name="来源网站", null=True)
    net_house_id = CharField(verbose_name="网站小区ID", max_length=50, null=False)
    house_id = IntegerField(verbose_name="楼盘ID", null=True, default=0)
    net_house_name = CharField(verbose_name="网站小区名称", max_length=100, null=False)
    edit_time = IntegerField(verbose_name="修改时间戳", null=True, default=0)
    class Meta:
        table_name = 'house_info_mapping'
        primary_key = CompositeKey('net_id', 'net_house_id')

# 出售房源
class HouseSaleItem(scrapy.Item):
    net_id = scrapy.Field()  # 来自网站
    sale_order_no = scrapy.Field() # 房源网站编号，唯一
    net_url = scrapy.Field()  # 详细网址
    net_house_id = scrapy.Field() # 网站小区ID
    net_house_name = scrapy.Field() # 网站小区名称
    title = scrapy.Field() # 标题
    room_name = scrapy.Field() # 房型
    room_num = scrapy.Field() # 几房：数字
    build_type = scrapy.Field()  # 建筑楼层，低，中，高
    total_floor = scrapy.Field()  # 总楼层
    area = scrapy.Field() # 面积
    build_year = scrapy.Field() # 建成年限
    direction = scrapy.Field() # 朝向
    fitment = scrapy.Field() # 装修
    district_name = scrapy.Field() # 区域
    plate_name = scrapy.Field() # 板块
    price = scrapy.Field() # 单价
    totalprice = scrapy.Field() # 总价
    gp_date = scrapy.Field() # 挂牌日期
    gp_year = scrapy.Field()  # 挂牌日期-年
    gp_month = scrapy.Field()  # 挂牌日期-月
    house_use = scrapy.Field() # 房屋用途
    house_attribute = scrapy.Field() # 产权属性
    add_time = scrapy.Field() # 添加时间戳
    edit_time = scrapy.Field() # 修改时间戳
    item_type = scrapy.Field() # item 类型

class HouseSaleModel(BaseModel):
    net_id = SmallIntegerField(verbose_name="来源网站", null=True)
    sale_order_no = CharField(verbose_name="房源网站编号，唯一", max_length=50, null=True)
    net_url = CharField(verbose_name="详细网址", max_length=100, null=False)
    net_house_id = CharField(verbose_name="网站小区ID", max_length=50, null=False)
    house_id = IntegerField(verbose_name="楼盘ID", null=True, default=0)
    net_house_name = CharField(verbose_name="网站小区名称", max_length=100, null=False)
    title = CharField(verbose_name="标题", max_length=100, null=False)
    room_name = CharField(verbose_name="房型", max_length=20, null=False)
    room_num = SmallIntegerField(verbose_name="几房：数字", null=True, default=0)
    build_type = CharField(verbose_name="建筑楼层，低，中，高", max_length=50, null=False)
    total_floor = CharField(verbose_name="总楼层", max_length=50, null=False)
    area = DecimalField(verbose_name="面积", null=True, default=0)
    build_year = CharField(verbose_name="建成年限", max_length=50, null=False)
    direction = CharField(verbose_name="朝向", max_length=50, null=False)
    fitment = CharField(verbose_name="装修", max_length=50, null=False)
    district_name = CharField(verbose_name="区域", max_length=50, null=False)
    plate_name = CharField(verbose_name="板块", max_length=50, null=False)
    price = IntegerField(verbose_name="单价", null=True, default=0)
    totalprice = IntegerField(verbose_name="总价", null=True, default=0)
    gp_date = DateField(verbose_name="挂牌日期", null=False)
    gp_year = IntegerField(verbose_name="挂牌日期-年", null=True, default=0)
    gp_month = IntegerField(verbose_name="挂牌日期-月", null=True, default=0)
    house_use = CharField(verbose_name="房屋用途", max_length=100, null=False)
    house_attribute = CharField(verbose_name="产权属性", max_length=100, null=False)
    is_deal = IntegerField(verbose_name="是否下架或出售：1：下架,0未下架", null=True, default=0)
    xj_date = DateField(verbose_name="下架日期", null=True,default=None)
    xj_year = IntegerField(verbose_name="下架日期-年", null=True, default=0)
    xj_month = IntegerField(verbose_name="下架日期-月", null=True, default=0)
    add_time = IntegerField(verbose_name="添加时间戳", null=True, default=0)
    edit_time = IntegerField(verbose_name="修改时间戳", null=True, default=0)
    class Meta:
        table_name = 'house_sale'
        primary_key = CompositeKey('net_id', 'sale_order_no')

# 出售房源带看信息
class HouseSaleVisitItem(scrapy.Item):
    net_id = scrapy.Field() # 来源ID
    sale_order_no = scrapy.Field() # 房源ID
    visit_date = scrapy.Field() # 带看日期
    visit_year = scrapy.Field()  # 带看日期-年
    visit_month = scrapy.Field()  # 带看日期-月
    visit_economic_id = scrapy.Field() # 带看经纪人
    visit_num   = scrapy.Field() # 带看次数
    add_time = scrapy.Field() # 添加时间戳
    item_type = scrapy.Field()  # item 类型

class HouseSaleVisitModel(BaseModel):
    net_id = SmallIntegerField(verbose_name="来源网站", null=True)
    sale_order_no = CharField(verbose_name="房源网站编号，唯一", max_length=50, null=True)
    visit_date = DateField(verbose_name="带看日期", null=True,default=None)
    visit_year = IntegerField(verbose_name="带看日期-年", null=True, default=0)
    visit_month = IntegerField(verbose_name="带看日期-月", null=True, default=0)
    visit_economic_id = CharField(verbose_name="带看经纪人编号", max_length=50, null=False)
    visit_num = IntegerField(verbose_name="带看次数", null=True, default=0)
    add_time = IntegerField(verbose_name="添加时间戳", null=True, default=0)
    class Meta:
        table_name = 'house_sale_visit'
        primary_key = CompositeKey('net_id', 'sale_order_no','visit_economic_id','visit_num')

# 出租房源
class HouseRentItem(scrapy.Item):
    house_rent_id = scrapy.Field() # 自增ID
    net_id = scrapy.Field()  # 来自网站
    rent_order_no = scrapy.Field() # 租房编号
    title = scrapy.Field()  # 标题
    room_name = scrapy.Field()  # 房型
    room_num = scrapy.Field()  # 几房：数字
    gp_date = scrapy.Field()  # 挂牌日期
    price = scrapy.Field() # 元/月
    area = scrapy.Field() # 面积
    direction = scrapy.Field()  # 朝向
    fitment = scrapy.Field()  # 装修
    build_type = scrapy.Field()  # 建筑楼层，低，中，高
    total_buile = scrapy.Field()  # 总楼层