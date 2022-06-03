import scrapy
from scrapy.crawler import CrawlerProcess
from wiki.wiki.spiders import wiki


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(wiki.WikiSpider)
    process.start()