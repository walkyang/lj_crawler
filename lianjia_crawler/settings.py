# -*- coding: utf-8 -*-

# Scrapy settings for lianjia_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime

BOT_NAME = 'lianjia_crawler'

SPIDER_MODULES = ['lianjia_crawler.spiders']
NEWSPIDER_MODULE = 'lianjia_crawler.spiders'

#to_day = datetime.datetime.now()
#log_file_path = "log/scrapy_{}_{}_{}.log".format(to_day.year,to_day.month,to_day.day)

#LOG_LEVEL = "WARNING"
#LOG_FILE = log_file_path

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianjia_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianjia_crawler.middlewares.LianjiaCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #'lianjia_crawler.middlewares.LianjiaCrawlerDownloaderMiddleware': 543,
    'lianjia_crawler.middlewares.LianjiaCrawlerUserAgentMiddleware': 543,
    'lianjia_crawler.middlewares.LianjiaCrawlerProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'lianjia_crawler.pipelines.LianjiaCrawlerPipeline': 300,
}

""" 启用限速设置 """
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 0.01  # 初始下载延迟
#DOWNLOAD_DELAY = 0.005  # 每次请求间隔时间

RANDOMIZE_DOWNLOAD_DELAY=False
DOWNLOAD_DELAY=60/300.0
CONCURRENT_REQUESTS_PER_IP=300

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

WXLJ_APP_ID = "ljwxapp:"
WXLJ_APP_KEY = "6e8566e348447383e16fdd1b233dbb49"

MYSQL_SETTING = "{'310000':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'sh','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'110000':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'bj','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'330100':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'hz','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'320500':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'suzhou','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'320200':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'wuxi','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'320583':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'ks','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'330200':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'nb','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'330400':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'jx','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'330600':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'sx','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'320400':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'changzhou','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'321100':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'zj','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'320100':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'nj','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'320300':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'xz','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'320900':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'yc','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}," \
                "'340100':{'MYSQL_HOST':'127.0.0.1','MYSQL_DBNAME':'hf','MYSQL_USER':'root','MYSQL_PASSWORD':'123456','MYSQL_PORT':3306}}"
