# -*- coding: utf-8 -*-
from os import name
import scrapy
import logging
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #1
        # title = response.xpath("//h1/text()").get()
        # country = response.xpath("//td/a/text()").getall()

        # yield{
        #     'Title':title,
        #     'Country':country
        # }

        #2
        # countries = response.xpath("//td/a")
        # for c in countries:
        #     name = c.xpath(".//text()").get() #when there is no response use.//
        #     link = c.xpath(".//@href").get()

        #     yield{
        #     'Name':name,
        #     'Country_Link':link
        # }

        countries = response.xpath("//td/a")
        for c in countries:
            name = c.xpath(".//text()").get()
            link = c.xpath(".//@href").get()
            # absolute url contais domain name and protocols like https
            # absolute_url = f'https://www.worldometers.info/{link}' #not a good approch
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url) #ctrl+c to stop
            yield response.follow(url=link, callback=self.parse_country, meta = {'countryname': name})
        #yield response.follow(url="https://www.worldometers.info/world-population/china-population/", callback=self.parse_country, meta = {'countryname': 'China'})
        #yield response.follow(url="https://www.worldometers.info/world-population/china-population/", callback=self.parse_country, meta = {'countryname': name})

    def parse_country(self, response):
        #inspect_response(response,self)
        #open_in_browser(response)
        #logging.info(response.status)
        #logging.info(response.url)
        name = response.request.meta['countryname']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for r in rows:
            year = r.xpath('.//td[1]/text()').get()
            ppltion = r.xpath('.//td[2]/strong/text()').get()
            yield {
                'Cname':name,
                'Year':year,
                'Population':ppltion
            }

       

        













        
