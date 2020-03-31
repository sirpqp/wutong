import copy
import os
import time

from settings import BASE_DIR

try:
    from settings import DEBUG
except ImportError:
    DEBUG = False


def add_settings_to_spider(spider_cls, settings: dict):
    """为 spider 添加设置并返回 spider

    注意：
        如果设置中含有字典，且 spider.custom_settings 有同项设置
        则会更新 （即调用 dict 的 `update` 方法）
        否则会覆盖

    """
    s = copy.deepcopy(settings)
    cus_settings = spider_cls.custom_settings
    if cus_settings:
        for k, v in cus_settings.items():
            if isinstance(v, dict) and k in s:
                s[k].update(v)
            else:
                s[k] = v
    spider_cls.custom_settings = s
    return spider_cls


def check_js_redirect(spider_cls):
    settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'lzz.downloadermiddlewares.jsredirect.JavaScriptRedirectMiddleware': 80
        }
    }
    return add_settings_to_spider(spider_cls, settings)


def get_log_settings(dirname=None, level=None, filename_format='%Y%m%d'):
    """返回日志相关设置"""
    if DEBUG:
        return {'LOG_LEVEL': 'DEBUG'}

    if not dirname:
        return {}

    dirname = os.path.join(BASE_DIR, f'logs/spiders/{dirname}')
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    file = f'{time.strftime(filename_format)}.log'
    path = os.path.join(dirname, file)
    level = level or 'INFO'
    return {'LOG_FILE': path, 'LOG_LEVEL': level}


def get_image_settings(dirname, urls_field='image_urls', result_field='images'):
    """返回图片下载相关设置

    :param dirname: 图片存放的文件夹名，用于存储文件和加载图片 pipeline
    :param urls_field: 存放图片 url 的字段，用于 pipeline 处理
    :param result_field: 存放图片下载结果的字段
    """
    # lzz/download/images/...
    path = os.path.join(BASE_DIR, f'download/images/{dirname}')
    settings = {
        'IMAGES_URLS_FIELD': urls_field,
        'IMAGES_RESULT_FIELD': result_field,
        'IMAGES_STORE': path
    }
    return settings
