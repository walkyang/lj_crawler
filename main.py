# -*- coding: utf-8 -*-
from scrapy import cmdline
# -L INFO关闭DEBUG信息
#cmdline.execute('scrapy crawl lianjia_crawler_spider'.split())
#cmdline.execute('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=310000 -a city_code=sh'.split())
#cmdline.execute('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=330100 -a city_code=hz'.split())
cmdline.execute('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320200 -a city_code=wx'.split())

'''
# 多个一起跑
import os
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=310000 -a city_code=sh')  # 上海
#os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=110000 -a city_code=bj')  # 北京
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=330100 -a city_code=hz')  # 杭州
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320500 -a city_code=su')  # 苏州
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320200 -a city_code=wx')  # 无锡
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320583 -a city_code=ks')  # 昆山

os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=330200 -a city_code=nb')  # 宁波
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=330400 -a city_code=jx')  # 嘉兴
#os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=330421 -a city_code=jiashan')  # 嘉善 "nh_only": 1
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=330600 -a city_code=sx')  # 绍兴

os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320400 -a city_code=changzhou')  # 常州
#os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=321000 -a city_code=yz')  # 扬州
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=321100 -a city_code=zj')  # 镇江
#os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320681 -a city_code=qidong')  # 启东

os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320100 -a city_code=nj')  # 南京
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320300 -a city_code=xz')  # 徐州
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320900 -a city_code=yc')  # 盐城
#os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=320700 -a city_code=lyg')  # 连云港
os.system('scrapy crawl lianjia_crawler_spider -L INFO -a city_id=340100 -a city_code=hf')  # 合肥
'''
