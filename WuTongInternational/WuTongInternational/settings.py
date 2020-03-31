# -*- coding: utf-8 -*-

import os
from fake_useragent import UserAgent

# Scrapy settings for WuTongInternational project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

ua = UserAgent()

BOT_NAME = 'WuTongInternational'

SPIDER_MODULES = ['WuTongInternational.spiders']
NEWSPIDER_MODULE = 'WuTongInternational.spiders'

# Project root
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'WuTongInternational (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'User-Agent': ua.random,
#   'Host': 'inter.chinawutong.com',
#   'Upgrade-Insecure-Requests': '1',
#   'Cookie': 'ASP.NET_SessionId=bmy1bhqdxpo2ic3n4piujpy5'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
   # 'WuTongInternational.middlewares.WutonginternationalSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'WuTongInternational.middlewares.WutonginternationalDownloaderMiddleware': 543,
    'WuTongInternational.middlewares.RandomProxyMiddleware': 80,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'WuTongInternational.pipelines.WutonginternationalPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IPS = ['39.137.69.9:80',
           '39.137.107.98:8080',
           '39.137.107.98:80',
           '39.137.69.9:8080',
           '39.137.95.73:8080',
           '39.137.95.74:80',
           '39.137.95.75:8080',
           '39.137.95.72:80',
           '39.137.95.70:80',
           '39.137.95.69:8080',
           '39.137.69.6:80',
           '39.137.69.6:8080',
           '123.207.217.104:1080',
           '39.137.69.10:80',
           '118.24.88.240:1080',
           '39.137.95.75:80',
           '39.137.95.69:80',
           '123.207.66.220:1080',
           '140.143.152.93:1080',
           '140.143.156.166:1080',
           '118.24.127.144:1080',
           '139.199.201.249:1080',
           '39.137.69.10:8080',
           '39.137.95.71:8080',
           '39.137.95.73:80',
           '39.137.95.72:8080',
           '140.143.137.69:1080',
           '140.143.142.218:1080',
           '123.207.218.215:1080',
           '123.207.217.139:1080',
           '118.89.150.177:1080',
           '116.114.19.211:443',
           '111.231.12.253:1080',
           '51.158.172.165:8811',
           '51.158.114.177:8811',
           '109.75.67.17:44151',
           '177.0.153.66:80',
           '45.137.217.27:80',
           '103.105.127.9:84',
           '103.47.13.41:8080',
           '103.211.8.221:44581',
           '121.237.149.85:3000',
           '118.25.16.35:1080',
           '110.243.0.164:9999',
           '131.196.143.225:33729',
           '103.87.236.169:8080',
           '185.89.0.229:34927',
           '163.172.152.52:8811',
           '185.238.239.103:8090',
           '163.204.245.182:9999',
           '125.62.193.5:83',
           '150.107.143.61:9797',
           '150.107.22.214:8080',
           '117.252.217.175:60722',
           '118.99.94.35:8080']
