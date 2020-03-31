# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import settings


class WutonginternationalSpiderMiddleware(object):
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


class WutonginternationalDownloaderMiddleware(object):
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


from collections import defaultdict


class RandomProxyMiddleware(object):

    # 初始化数据
    def __init__(self, settings):
        self.settings = settings
        self.ips = settings.getlist("IPS")
        # 错误记录   转成字典结构（value是int类型） 默认为0
        self.proxy_error_stats = defaultdict(int)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        # 实例化的时候，把settings给init函数
        s = cls(crawler.settings)
        # 实例化的时候注册了个信号
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
        # 加代理IP
        if "proxy" not in request.meta:
            proxy = random.choice(self.ips)
            # proxy = random.choice(self.cookies)
            # proxy = random.choice(self.headers)
            print(proxy, "---------------------------------")
            request.meta['proxy'] = 'http://' + proxy
        # else:
        #     print(request.meta["proxy"])
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        status_code = response.status
        if status_code in [403, 500, 404, 502, 429]:
            ip = request.meta["proxy"]
            # 统计某个IP的错误次数
            self.proxy_error_stats[ip] += 1
            # 如果大于我们约定的五次，那就删IP
            if self.proxy_error_stats[ip] > 5:
                self.ips.remove(ip)
                self.remove_fail_ip(ip)
                # 去掉这个请求的meta的proxy
                del request.meta["proxy"]
            return request
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        # 当出现跟代理IP有关系的异常的时候
        if isinstance(exception, (ConnectionRefusedError, TimeoutError)):
            # self.ips 去掉这个无效的IP
            ip = request.meta["proxy"]
            # self.ips.remove(ip)
            self.remove_fail_ip(ip)
            # 去掉这个请求的meta的proxy
            del request.meta["proxy"]
            # 重新安排下载
            return request

    def remove_fail_ip(self, ip):
        if ip in self.ips:
            self.ips.remove(ip)

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)