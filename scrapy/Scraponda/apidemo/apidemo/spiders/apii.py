# -*- coding: utf-8 -*-
import scrapy
import json

class ApiiSpider(scrapy.Spider):
    name = 'apii'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        res = json.loads(response.body)
        quotes = res.get('quotes') #res['quotes'] 
        for q in quotes:
            yield{
                'author':q.get('author').get('name'),
                'tag':q.get('tags'),
                'quote':q.get('text')
            }

        next = res.get('has_next')
        if next:
            next_pg_no = res.get('page')+1
            yield scrapy.Request(url = f'http://quotes.toscrape.com/api/quotes?page={next_pg_no}',callback=self.parse)
