import scrapy

class NewsprimeSpider(scrapy.Spider):
    name = 'newsprime'
    start_urls = ['http://www.newsprime.co.kr/news/section_list_all/?sec_no=66&page=2']

    def parse(self, response):
        for news in response.css('.td.news1'):
            print("뉴스: ",news)