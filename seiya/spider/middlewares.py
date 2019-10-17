# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware as _UserAgentMiddleware
import random

class UserAgentMiddleware(_UserAgentMiddleware):
    user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
            "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
            "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
            "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
            "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
            "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
            "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
            "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
            "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
            "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
            "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
            ]

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if spider.name == 'jobs':
            if ua:
                print('******UesrAgent:{}******'.format(ua))
                request.headers.setdefault('User-Agent', ua)
                request.headers.setdefault('Host', 'www.lagou.com')
                request.headers.setdefault('Cookie', 'JSESSIONID=ABAAABAAADEAAFIAF037B646FF75E78F6464F4B9A62FC29; user_trace_token=20191010090442-a62a051e-e45f-4449-b2d2-626aa201a683; WEBTJ-ID=20191010090330-16db33138082e1-0c32c14b401252-3c375f0d-2073600-16db33138095db; _ga=GA1.2.1985291566.1570669410; _gid=GA1.2.1395848530.1570669410; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216db33139aa899-00dbec05cf3572-3c375f0d-2073600-16db33139aba31%22%2C%22%24device_id%22%3A%2216db33139aa899-00dbec05cf3572-3c375f0d-2073600-16db33139aba31%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570669411; LGUID=20191010090443-f1eed058-eaf9-11e9-99a6-525400f775ce; SEARCH_ID=5bc3a38e1899421ca7a1145e311f323f; LGSID=20191010151851-35b32102-eb2e-11e9-99c0-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=80d07a25cee4e8873202960751d221bac43f7f1a82; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570691968; LGRID=20191010152040-76c1f4b4-eb2e-11e9-99c0-525400f775ce')
        elif spider.name == 'houses':
            if ua:
                print('******UesrAgent:{}******'.format(ua))
                request.headers.setdefault('User-Agent', ua)
                request.headers.setdefault('Host', 'gy.lianjia.com')
                request.headers.setdefault('Cookie', 'lianjia_uuid=6e88dc26-d5a7-44b4-9f0b-31d53ef00bd2; _smt_uid=5da6cd77.92861d1; UM_distinctid=16dd3929b937c0-0fdccd515b0b22-3c375f0d-1fa400-16dd3929b9449d; _jzqa=1.983898288894835600.1571212664.1571212664.1571212664.1; _jzqc=1; _jzqx=1.1571212664.1571212664.1.jzqsr=cd%2Elianjia%2Ecom|jzqct=/zufang/.-; _jzqckmp=1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216dd3929c8f86-0926b6772fd0ae-3c375f0d-2073600-16dd3929c90a18%22%2C%22%24device_id%22%3A%2216dd3929c8f86-0926b6772fd0ae-3c375f0d-2073600-16dd3929c90a18%22%2C%22props%22%3A%7B%7D%7D; _ga=GA1.2.34693991.1571212666; _gid=GA1.2.1558603043.1571212666; select_city=520100; all-lj=762328e22710c88ff41f391dedabbc6f; CNZZDATA1254525948=715804443-1571211097-https%253A%252F%252Fwww.lianjia.com%252F%7C1571211097; CNZZDATA1255633284=1572664829-1571208789-https%253A%252F%252Fwww.lianjia.com%252F%7C1571208789; CNZZDATA1255604082=764595384-1571211541-https%253A%252F%252Fwww.lianjia.com%252F%7C1571211541; _qzja=1.1359645162.1571212840721.1571212840721.1571212840722.1571212840721.1571212840722.0.0.0.1.1; _qzjc=1; _qzjto=1.1.0; lianjia_ssid=9772637b-4d87-4bdf-8e24-42123656c8dc; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiM2UwZmYwZjEyZjc5ZTliNTI1NjI0NmY1YWQyMjI4N2VkYTVkZjZjZTNhMDBhMTAyMzQ1NmZkODhkNjA5MDdiNTllMWI3ODQzZTBiMzM0MmMxMjM2ZWQ2MzRjODBjYzdjMGE4Mzk3NWRhZmMwM2MzMDcwMDQzMWZmODJjNjQzNDBjZmM4ZmNjZWVmYmM5NjZkY2RmOTg3ZTM5MmNiZjdmZGE0M2M4YjMyZGI3MDk1MGFiY2YzMjQ0NzcyNTQ5ZmY4MjdiNTJkZDYzYTU3MmQyYTM0MGFkZDEzN2Q3MGZlNGRmMDc1Mjg0OWFkYzJjOGMzYjA2ODYzNzJmNWEwOWU0NGI3NDM5Y2Y3NDBjZDRlNjRjMzUyNTkzZjBhNGMxNzAyOWNmOTRkOTRiNWUzOTBhN2JhMmNjYzk2MjY1YTdjYjNcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiODJiMjFiYWJcIn0iLCJyIjoiaHR0cHM6Ly9neS5saWFuamlhLmNvbS96dWZhbmcvcGcxcnQyMDA2MDAwMDAwMDEvJTNFIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=')


class SpiderSpiderMiddleware(object):
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

        # Should return either None or an iterable of Response, dict
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


class SpiderDownloaderMiddleware(object):
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
