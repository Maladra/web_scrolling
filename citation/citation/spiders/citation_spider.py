import scrapy

class CitationSpider(scrapy.Spider):
    name="citation"
    start_urls = ['http://www.1001-citations.com/page/1/',]

    def parse(self, response):
        for quote in response.css('div.entry'):
            yield {
                'text' : quote.css('h2 ::text').get(),
                'author' : quote.css('span.author ::text').getall(),
            }

        next_page = response.css('a.nextpostslink::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
