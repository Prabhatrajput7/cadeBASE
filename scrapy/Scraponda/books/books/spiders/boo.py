import scrapy

class BooSpider(scrapy.Spider):
    name = 'boo'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):

        for p in response.xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']"):
            yield{
                'Title': p.xpath(".//article[@class='product_pod']/h3/a/@title").get(),
                'Link': response.urljoin(p.xpath(".//article[@class='product_pod']/h3/a/@href").get()),
                'Price': p.xpath(".//article[@class='product_pod']/div[2]/p/text()").get(),
                'Stock': p.xpath(".//article[@class='product_pod']/div[2]/p[2]/text()").extract()[1].strip()
            }
        next_pg = response.urljoin(response.xpath("//li[@class='next']/a/@href").get())

        if next_pg:
            yield scrapy.Request(url=next_pg, callback=self.parse)

    
