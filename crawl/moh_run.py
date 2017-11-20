from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from crawl.spiders.moh_spider import MohSpider





def setup_crawler(domain):
    spider =MohSpider(domain=domain)
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(spider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

if __name__ == '__main__':
    setup_crawler(None)
