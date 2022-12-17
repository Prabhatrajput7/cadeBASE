import scrapy
from scrapy import FormRequest
# when ever working woth form check for input id hidden data
class RealloginSpider(scrapy.Spider):
    name = 'reallogin'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login/']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formid='register',
            formdata={
                'username': 'sony789632145@gmail.com',
                'password': 'sonysony',
                'redirect': '/',
                'debug_token': '',
                'login': 'Log In'
            },
            callback=self.after_login
        )
    
    def after_login(self, response):
        print('logged in...')
