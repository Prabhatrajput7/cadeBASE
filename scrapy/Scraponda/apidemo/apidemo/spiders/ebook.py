import scrapy
import json
from scrapy.exceptions import CloseSpider
class EbookSpider(scrapy.Spider):
    name = 'ebook'
    incremented = 12
    offset = 0
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12']

    def parse(self, response):
        if response.status == 500:
            raise CloseSpider('Reached Last Page')
        res = json.loads(response.body)
        ebooks = res.get('works')
        for e in ebooks:
            yield{
                'title': e.get('title'),
                'subject':e.get('subject')
            }
        self.offset+=self.incremented
        yield scrapy.Request(url=f'https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}', callback=self.parse)