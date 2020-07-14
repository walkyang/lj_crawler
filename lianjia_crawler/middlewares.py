# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class LianjiaCrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LianjiaCrawlerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



import hashlib
import base64
from urllib.parse import urlparse, parse_qs
import time
import random
# wx链家头部处理
LJ_headers = {
        'charset': "utf-8",
        'time-stamp': str(time.time()*1000)[:13],
        'lianjia-openid': "oYveJ5SZSLfxYQNQ83v8KNjrRvyc",
        'cookie': "lianjia_token=",
        'srcid': "eyJ0IjoiZXlKdmN5STZJbmQ0WVhCd0lpd2lkQ0k2SW0xRGIydFRTVEEyWVROTGNrdDBNSFptY0ZwQkswZFZNRmhqWjFWb2RGcE1aRXR3ZG14dmVUUmlZbFJWWnpZeFREWXJiR0p4YkdWVFN6bDRRMWh2V0hOUE9FZzRWVEJ3Y2tFNGRFcGthelZuYzBOWUwyZEJQVDBpTENKMklqb2liVnBDUVUxMU4yMDFja1ZYUVhObVIwZHBaakZVY0QwOUlpd2ljR0Z5ZEc1bGNpSTZJbUpsYVd0bGVtWWlmUT09IiwiciI6Im9ZdmVKNVNaU0xmeFlRTlE4M3Y4S05qclJ2eWMiLCJvcyI6Ind4YXBwIiwidiI6IjAuMC4xIn0=",
        'lianjia-wxminiapp-version': "5.6.1",
        'lianjia-fourandone': "1",
        'content-type': "application/json",
        'referer': "https://servicewechat.com/wxcfd8224218167d98/76/page-frame.html",
        'wx-version': "7.0.6",
        'lianjia-xcxsource': "otherxcx_lianjia",
        'wxminiapp-sdk-version': "2.8.0",
        'city-id': "310000",
        'lianjia-source': "ljwxapp",
        'lianjia-xcxscene': "1089",
        'lianjia-session': "",
        'os-version': "android-Android 5.0",
        'lianjia-uuid': "8235d1f841214b275b766657469153c7",
        'User-Agent': "Mozilla/5.0 (Linux; Android 5.0; SM-N9006 Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand0 NetType/WIFI Language/zh_CN",
        'Host': "wx.api.ke.com",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "e198f5e1-e77d-4c05-8086-81c3186fd2d8,53394b16-9068-469d-82a8-1f01f7f303e6",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
# wx链家Middleware
class LianjiaCrawlerUserAgentMiddleware(object):
    def __init__(self,wxlj_app_id,wxlj_app_key):
        self.wxlj_app_id = wxlj_app_id
        self.wxlj_app_key = wxlj_app_key
        self.user_agents = [
            'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'
        ]

    @classmethod
    def from_settings(cls, settings):
        return cls(wxlj_app_id=settings['WXLJ_APP_ID'],
                   wxlj_app_key=settings['WXLJ_APP_KEY'])

    # 生成authorization
    def _get_authorization(self,url):
        param = ""
        parse_param = parse_qs(urlparse(url).query, keep_blank_values=True)  # 解析url参数
        data = {key: value[-1] for key, value in parse_param.items()}  # 生成字典
        dict_keys = sorted(data.keys())  # 对key进行排序
        for key in dict_keys:  # 排序后拼接参数,key = value 模式
            param += str(key) + "=" + data[key]
        param = param + self.wxlj_app_key  # 参数末尾添加app_key
        param_md5 = hashlib.md5(param.encode()).hexdigest()  # 对参数进行md5 加密
        authorization_source = self.wxlj_app_id + param_md5  # 加密结果添加前缀app_id
        authorization = base64.b64encode(authorization_source.encode())  # 再次进行base64 编码
        return authorization.decode()

    def process_request(self, request, spider):
        if 'wx-api.zu.ke' in request.url:
            request.headers['User-Agent'] = random.choice(self.user_agents)
        else:
            authorization = self._get_authorization(request.url)
            for key, value in LJ_headers.items():
                request.headers['{}'.format(key)] = value
            request.headers['authorization'] = authorization

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"
# 代理隧道验证信息
proxyUser = "xxxxxxx"
proxyPass = "xxxxxxx"
# wx链家proxy Middleware
class LianjiaCrawlerProxyMiddleware(object):
    def process_request(self, request, spider):
        proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth