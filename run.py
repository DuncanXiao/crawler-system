import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]').getall():
            print('--------')
            print(quote.xpath('/span[@class="text"]/text()').get())
            # yield {
            #     'text': quote.xpath('/span[@class="text"]/text()').get(),
            #     'author': quote.xpath('/span/small[@class="author"]/text()').get(),
            # }
        # print(response.xpath('//div[@class="quote"]/span[@class="text"]/text()').get())
        # print('sssss----======')
        # print(response.css('div.quote'))
        # print('--------')
        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)