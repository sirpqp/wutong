"""
Start crawl spider.
"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from parsetools.spider import iter_spider_from_module


def crawl(*spiders, stop_after_crawl=True):
    """Crawl spiders."""
    crawler_process = CrawlerProcess(get_project_settings())
    for spider in spiders:
        crawler_process.crawl(spider)
    crawler_process.start(stop_after_crawl)


class SchedulerCrawlerProcess(CrawlerProcess):
    """处理较多爬虫同时运行的情况

    爬虫较多的时候，如项目中的全国省份下各个爬虫
    并发运行会给数据库带来较大的压力
    所以使用调度器，让一个爬虫结束的时候，马上启动下一个爬虫
    直到所有爬虫运行完毕为止

    # >>> scheduler = SchedulerCrawlerProcess('lzz.spiders.news.anhui')
    # >>> scheduler.start(1)

    """

    def __init__(self, spider_module, settings=None, install_root_handler=True):
        self._spiders = iter_spider_from_module(spider_module)
        settings = settings or get_project_settings()
        super().__init__(settings, install_root_handler)

    def crawl(self, crawler_or_spidercls, *args, **kwargs):
        d = super().crawl(crawler_or_spidercls, *args, **kwargs)
        try:
            spider_cls = next(self._spiders)
            d.addBoth(lambda _: self.crawl(spider_cls))
        except StopIteration:
            pass
        return d

    def start(self, concurrent_spider=5, stop_after_crawl=True):
        try:
            for _ in range(concurrent_spider):
                spider_cls = next(self._spiders)
                self.crawl(spider_cls)
        except StopIteration:
            pass

        super().start(stop_after_crawl)


def run_spiders(spider_type, upload_after_crawl=True):
    """
    启动爬虫
    :param spider_type: 爬虫类型
        `news`  资讯
        `buy`   求购
        `news_policy`   政策快报资讯
        `huobiao`   火标网电梯招标信息
        `kuaibao`   工业快报数据

    :param upload_after_crawl:
        是否爬虫爬取完成后上传数据
    """
    from upload import (
        upload_buy, upload_news,
        upload_news_policy,
        upload_huobiao, upload_industry
    )

    # 爬虫类型对应的：爬虫文件所在路径与上传函数
    spider_upload_mappings = {
        'news': ('lzz.spiders.news', upload_news,),
        'news_policy': ('lzz.spiders.newspolicy', upload_news_policy,),
        'kuaibao': ('lzz.spiders.kuaibao', upload_industry,),
        'buy': ('lzz.spiders.buying', upload_buy,),
    }

    if spider_type == 'huobiao':
        # 火标网 单独处理
        from lzz.spiders.huobiao import HuoBiaoSpider

        crawl(HuoBiaoSpider)
        if upload_after_crawl:
            upload_huobiao()

    elif spider_type in spider_upload_mappings:
        module_str, upload_func = spider_upload_mappings[spider_type]
        scheduler = SchedulerCrawlerProcess(module_str)
        scheduler.start()
        if upload_after_crawl:
            upload_func()

    else:
        raise ValueError(f'Not support spider type: {spider_type}')
