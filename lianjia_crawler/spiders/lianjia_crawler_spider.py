# -*- coding: utf-8 -*-
import scrapy
import json
import math
import time
from datetime import datetime
from ..items import HouseSaleItem,HouseSaleVisitItem
import logging

class LianjiaCrawlerSpiderSpider(scrapy.Spider):
    name = 'lianjia_crawler_spider'
    allowed_domains = ['wx.api.ke.com','wx-api.zu.ke.com']
    #now_page = 0  # 设置一个全部变量当前页面
    base_url = 'https://wx.api.ke.com'
    zu_base_url = 'https://wx-api.zu.ke.com'
    #city_id = 31000

    def __init__(self, city_id=None,city_code=None, *args, **kwargs):
        super(LianjiaCrawlerSpiderSpider,self).__init__(*args, **kwargs)
        self.city_id = city_id
        self.city_code = city_code


    # https://wx-api.zu.ke.com/v1/config/filters?city_id=320200&ts=1566979982
    # https://wx.api.ke.com/ershoufang/search?city_id=310000&condition=d310115b611900123&query=&order=co32&offset=0&limit=10&from=search_result&sug_title=&areaName=%E5%8C%97%E8%94%A1&sign=
    def start_requests(self):
        ts = str(time.time())[0:10]
        start_urls = ['{zu_base_url}/v1/config/filters?city_id={city_id}&ts={ts}'.format(zu_base_url=self.zu_base_url,city_id=self.city_id,ts=ts)]
        # 主回调函数parse中--房源
        yield scrapy.Request(start_urls[0], callback=self.parse)
        # 次回调函数rentparse中--租房
        #yield scrapy.Request(self.start_urls[1], callback=self.lj_rent_parse)

    # 这里要从获得板块开始了...
    def parse(self,response):
        #logging.warning(response)
        r = json.loads(response.text)
        if r['msg'] == 'OK':
            for d in r['data']['d']['options']:# 得到区域
                for p in d['children']:# 得到板块
                    if p['id']:
                        #print(d['id'],p['id'],p['name'])
                        condition = 'd'+str(d['id'])+'b'+str(p['id'])
                        areaName = p['name']
                        yield scrapy.Request('{base_url}/ershoufang/search?city_id={city_id}&condition={condition}&query=&order=co32&offset=0&limit=10&from=search_result&sug_title=&areaName={areaName}&sign='
                                             .format(base_url=self.base_url,city_id=self.city_id,condition=condition,areaName=areaName),
                                             meta={'condition': condition,'areaName':areaName,'now_page':0},callback=self.lj_sale_parse)



    # 先运行房源信息首页，得到总条数循环页数
    def lj_sale_parse(self, response):
        logging.warning(response)
        r = json.loads(response.text)
        condition = response.meta['condition']
        areaName = response.meta['areaName']
        now_page = response.meta['now_page']
        if(r['error_code'] == 0):
            total_count = r['data']['total_count'] # 总条数，10条1页
            total_page = math.ceil(total_count/10) #总页数
            # 解析数据
            for i in r['data']['list']:
                housesale = HouseSaleItem()
                try:
                    i_house_sale = r['data']['list'][i]
                    housesale['net_id'] = 1  # 来自网站，链家web 1
                    housesale['net_url'] = 'https://'+self.city_code+'.ke.com/ershoufang/' + i_house_sale['house_code']+'.html' # 链接
                    housesale['sale_order_no'] = sale_order_no = i_house_sale['house_code'] # 房源ID
                    housesale['net_house_id'] = i_house_sale['resblock_id'] # 小区ID
                    housesale['net_house_name'] = i_house_sale['resblock_name'] # 小区名
                    housesale['title'] = i_house_sale['title'] # 标题
                    housesale['room_name'] = i_house_sale['frame_type'] # 房型
                    housesale['room_num'] = i_house_sale['frame_bedroom_num']  # 几房
                    housesale['build_type'] = i_house_sale['floor_level'] # 楼层
                    housesale['total_floor'] = i_house_sale['floor_total'] # 总楼层
                    housesale['area'] = i_house_sale['house_area'] # 面积
                    housesale['build_year'] = i_house_sale['building_year'] # 建成年限
                    housesale['direction'] = i_house_sale['orientation'] # 朝向
                    housesale['fitment'] = i_house_sale['decoration_type'] # 装修
                    housesale['district_name'] = i_house_sale['district_name'] # 区域
                    housesale['plate_name'] = i_house_sale['bizcircle_name'] # 板块
                    housesale['price'] = int(float(i_house_sale['unit_price'])) # 单价
                    housesale['totalprice'] = i_house_sale['total_price']*10000 # 总价
                    housesale['gp_date'] = i_house_sale['list_time'].replace('.','-') # 挂牌日期
                    housesale['gp_year'] = time.strftime('%Y', time.localtime(
                        time.mktime(datetime.strptime(str(housesale['gp_date']), '%Y-%m-%d').timetuple())))
                    housesale['gp_month'] = time.strftime('%m', time.localtime(
                        time.mktime(datetime.strptime(str(housesale['gp_date']), '%Y-%m-%d').timetuple())))
                    housesale['house_attribute'] = i_house_sale['deal_property'] # 房屋属性
                    housesale['house_use'] = i_house_sale['house_type'] # 房屋用途
                    # 添加日期
                    times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    time_array = time.strptime(times, "%Y-%m-%d %H:%M:%S")
                    time_stamp = int(time.mktime(time_array))
                    housesale['add_time'] = time_stamp
                    housesale['edit_time'] = time_stamp
                    housesale['item_type'] = 'house_sale'
                    # 数据保存
                    yield housesale
                except Exception as e:
                    logging.warning('Error:',e)
                # 进入近期带看记录
                # yield scrapy.Request("{base_url}/agent/display/ershoufang/takelook?house_code={sale_order_no}&city_id={city_id}&order_type=2&page_num=1&sign="
                #                      .format(base_url=self.base_url,sale_order_no=sale_order_no,city_id=self.city_id),
                #                      callback=lambda response, sale_order_no=sale_order_no: self.lj_visit_parse(response,sale_order_no))

            # 当前页数小于总页数，则继续循环下一页
            while now_page < total_page:
                now_page = now_page+1
                now_count = now_page * 10
                yield scrapy.Request(
                    '{base_url}/ershoufang/search?city_id={city_id}&condition={condition}&query=&order=co32&offset={offset}&limit=10&from=search_result&sug_title=&areaName={areaName}&sign='
                    .format(base_url=self.base_url, city_id=self.city_id, condition=condition, areaName=areaName,offset=now_count),
                    meta={'condition': condition, 'areaName': areaName, 'now_page': now_page}, callback=self.lj_sale_parse)
                break

    # 链家带看数据
    def lj_visit_parse(self, response, sale_order_no):
        res = json.loads(response.text)['data']['agent_list']
        if (res["total"] > 0):
            seeRecord = res["list"]
            for i in seeRecord:
                try:
                    i_see = res["list"][i]
                    housesale_visit = HouseSaleVisitItem()
                    housesale_visit['net_id'] = 1;
                    housesale_visit['sale_order_no'] = sale_order_no
                    housesale_visit['visit_date'] = i_see['time'].replace('/','-') # 最新带看时间
                    housesale_visit['visit_year'] = time.strftime('%Y', time.localtime(
                        time.mktime(datetime.strptime(housesale_visit['visit_date'], '%Y-%m-%d').timetuple())))
                    housesale_visit['visit_month'] = time.strftime('%m', time.localtime(
                        time.mktime(datetime.strptime(housesale_visit['visit_date'], '%Y-%m-%d').timetuple())))
                    housesale_visit['visit_economic_id'] = i_see['agent_ucid'] # 经纪人ID
                    housesale_visit['visit_num'] = i_see['this_house_see_count'] # 该房源带看次数
                    # 添加日期
                    times = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    time_array = time.strptime(times, "%Y-%m-%d %H:%M:%S")
                    time_stamp = int(time.mktime(time_array))
                    housesale_visit['add_time'] = time_stamp
                    housesale_visit['item_type'] = 'house_sale_visit'
                    yield housesale_visit
                except Exception as e:
                    logging.warning('Error:',e)

    # 租房数据解析
    def lj_rent_parse(self):
        pass