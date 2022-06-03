import scrapy


class WikiSpider(scrapy.Spider):
    name = "wiki"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Data_scraping',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for link in response.css('a'):
            print(link)
            yield {
                'link': link.css('a::attr(href)').get()
            }

