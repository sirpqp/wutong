"""
For Spider.
"""

from scrapy.utils.misc import walk_modules
from scrapy.utils.spider import iter_spider_classes

from parsetools.settings import add_settings_to_spider


def iter_spider_from_module(modules):
    """返回包含指定模块下的所有 spider 类的生成器"""
    for m in walk_modules(modules):
        yield from iter_spider_classes(m)


def add_url_field(spider_cls, field, start_requests, settings=None, allowed_domains=None):
    """爬虫类装饰器
    用于为 spider 添加特定的地址 这些地址满足统一的解析规则
    初期用于对今日头条、百度等网站爬虫（它们分类不同 但解析规则相同）

    :param spider_cls:
        spider object

    :param field:
        spider 中定义的类属性名称

    :param start_requests:
        对 field 中的 url 的处理函数
        该函数接收所有的 field 中的 url
        且返回可迭代的 request 实例

    :param settings:
        自定义设置，可以接收一个函数或字典
        如果传入的是函数，这个函数须以 spider_cls 为参数，并返回一个字典对象

    :param allowed_domains:
        允许的 domains

    """
    if not hasattr(spider_cls, field):
        name = spider_cls.__name__
        raise AttributeError(f'{name} missing attribute `{field}`')

    if settings is not None:
        spider_cls = add_settings_to_spider(spider_cls, settings)

    if allowed_domains is not None:
        if not hasattr(spider_cls, 'allowed_domains'):
            spider_cls.allowed_domains = list(allowed_domains)
        else:
            for d in allowed_domains:
                if d not in spider_cls.allowed_domains:
                    spider_cls.allowed_domains.append(d)

    super_start_requests = spider_cls.start_requests

    def _start_requests(spider):
        urls = getattr(spider, field)
        for request in start_requests(urls):
            yield request
        yield from super_start_requests(spider)

    spider_cls.start_requests = _start_requests

    return spider_cls
