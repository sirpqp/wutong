# -*- coding: utf-8 -*-

import os
import random
from fake_useragent import UserAgent

# Scrapy settings for WuTongInternational project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# ua = UserAgent()

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
DOWNLOAD_DELAY = round(random.random()*10, 2)
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
    # 'WuTongInternational.middlewares.WutonginternationalDownloaderMiddleware': 543,
    # 'WuTongInternational.middlewares.RandomProxyMiddleware': 80,
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

# MYSQL settings
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = '123456'
MYSQL_DATABASE = 'lzz'


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
       '118.99.94.35:8080',
       '182.34.33.117:9999',
       '125.110.117.21:9000',
       '122.5.107.50:9999',
       '171.12.42.151:9999',
       '122.4.40.54:9999',
       '114.226.163.153:9999',
       '125.108.101.179:9000',
       '220.176.92.223:9000',
       '1.198.108.194:9999',
       '123.54.52.174:9999',
       '123.54.44.106:9999',
       '117.91.251.104:9999',
       '123.169.118.53:9999',
       '118.112.194.224:9999',
       '113.194.136.23:9999',
       '123.101.215.2:9999',
       '171.35.223.39:9999',
       '113.121.36.91:9999',
       '223.199.30.40:9999',
       '117.95.199.53:9999',
       '122.5.107.137:9999',
       '123.169.119.158:9999',
       '175.42.128.240:9999',
       '123.54.46.226:9999',
       '125.110.92.184:9000',
       '113.195.17.195:9999',
       '171.13.103.155:9999',
       '120.83.111.19:9999',
       '175.161.19.122:9000',
       '49.86.182.179:9999',
       '115.218.209.168:9000',
       '60.13.42.79:9999',
       '1.199.30.209:9999',
       '121.233.207.152:9999',
       '125.108.84.21:9000',
       '180.118.128.137:9000',
       '110.243.2.236:9999',
       '1.196.105.192:9999',
       '106.42.216.104:9999',
       '125.108.76.53:9000',
       '113.195.22.66:9999',
       '110.243.27.72:9999',
       '125.108.126.108:9000',
       '125.110.124.141:9000',
       '183.166.21.34:9999',
       '182.46.87.32:9999',
       '183.166.70.236:9999',
       '183.166.170.184:8888',
       '114.239.147.111:9999',
       '171.13.203.95:9999',
       '125.110.88.179:9000',
       '117.91.130.52:9999',
       '223.199.26.125:9999',
       '125.123.159.127:44514',
       '1.199.31.18:9999',
       '117.85.21.12:9999',
       '175.44.108.240:9999',
       '123.169.119.150:9999',
       '183.166.103.240:9999',
       '58.253.157.142:9999',
       '122.5.191.132:9999',
       '171.13.4.158:9999',
       '125.108.104.63:9000',
       '113.121.189.177:24962',
       '120.83.100.121:9999',
       '171.13.202.43:9999',
       '123.169.119.32:9999',
       '49.70.95.146:9999',
       '125.110.118.214:9000',
       '125.108.74.88:9000',
       '112.84.48.244:9999',
       '1.198.73.218:9999',
       '123.169.101.182:9999',
       '122.192.175.105:9999',
       '123.101.212.235:9999',
       '49.86.178.92:9999',
       '103.219.143.135:8080',
       '123.169.97.48:9999',
       '118.212.106.85:9999',
       '123.169.162.10:9999',
       '114.99.160.50:27219',
       '125.108.67.71:9000',
       '222.189.144.205:9999',
       '171.15.49.220:9999',
       '122.234.91.143:9000',
       '125.87.111.49:39030',
       '125.108.95.90:9000',
       '110.243.30.245:9999',
       '123.160.99.54:9999',
       '110.243.17.248:9999',
       '110.243.23.250:9999',
       '125.78.216.130:31801',
       '183.166.103.133:9999',
       '171.11.28.161:9999',
       '123.52.97.114:9999',
       '121.233.207.219:9999',
       '1.193.246.42:9999',
       '125.108.91.220:9000',
       '113.138.135.219:29206',
       '117.91.131.143:9999',
       '58.253.156.116:9999',
       '125.108.114.39:9000',
       '171.15.65.44:9999',
       '123.54.47.168:9999',
       '123.169.126.49:9999',
       '182.46.123.151:9999',
       '113.194.28.221:9999',
       '125.110.69.155:9000',
       '175.42.128.2:9999',
       '220.179.102.151:34112',
       '123.54.45.84:9999',
       '171.35.149.158:9999',
       '175.44.109.93:9999',
       '114.239.42.105:9999',
       '222.85.101.177:22661',
       '114.224.47.35:9999',
       '163.204.95.24:9999',
       '125.108.83.145:9000',
       '119.108.160.248:9000',
       '1.197.11.190:9999',
       '125.110.96.94:9000',
       '123.179.165.136:26951',
       '163.204.243.26:9999',
       '125.108.103.235:9000',
       '183.166.102.165:9999',
       '163.204.247.45:9999',
       '117.91.250.212:9999',
       '171.13.137.19:9999',
       '175.42.128.241:9999',
       '123.134.118.163:38277',
       '123.54.44.230:9999',
       '171.11.178.225:9999',
       '117.91.254.28:9999',
       '182.34.23.42:9999',
       '121.232.199.137:9000',
       '123.169.164.49:9999',
       '125.110.72.79:9000',
       '114.239.145.31:9999',
       '180.125.120.2:41458',
       '171.12.113.6:9999',
       '123.169.164.54:9999',
       '123.169.112.105:9999',
       '171.13.201.71:9999',
       '117.88.176.188:3000',
       '1.197.204.98:9999',
       '123.163.122.204:9999',
       '223.242.224.17:9999',
       '121.232.199.102:9000',
       '123.54.46.169:9999',
       '119.250.103.211:24058',
       ]
