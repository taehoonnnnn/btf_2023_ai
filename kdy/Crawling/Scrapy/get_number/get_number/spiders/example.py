import scrapy

class MySpider(scrapy.Spider):
    name = "get_number"
    start_urls = ["http://www.newsprime.co.kr/news/section_list_all/?sec_no=66&page=2"]  # 크롤링을 시작할 웹 사이트 주소를 여기에 입력하세요

    def parse(self, response):
        print("출력: ", response.body.decode('utf-8'))
        # # 클래스 이름이 "c011_area"인 모든 <a> 태그를 선택합니다
        # links = response.css('a.c011_area::attr(href)').getall()
        # print("링크:", links)

