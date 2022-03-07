import scrapy
from ..items import DemoItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]


    def parse(self, response):
        all_quotes_div = response.css("div.quote")  # extracts our target source code

        items = DemoItem()

        for quote in all_quotes_div:

            title = quote.css('span.text::text').extract()
            author= quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag


            yield items

