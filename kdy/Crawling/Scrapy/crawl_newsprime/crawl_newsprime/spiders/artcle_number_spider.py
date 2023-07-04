import scrapy
from datetime import datetime

class MySpider(scrapy.Spider):
    name = 'num'
    article_num = 605756
    start_urls = ['http://www.newsprime.co.kr/news/article/?no=' + str(article_num)]

    def parse(self, response):
        # 제목을 추출한다
        titles = response.css('.title::text').getall()
        # 소제목을 추출한다
        subtitles = response.css('.subtitle::text').getall()     

        # 기자와 날짜/시간을 추출한다
        arvdate = response.css('.arvdate').get()
        arvdate_selector = scrapy.Selector(text=arvdate)
        journalist = arvdate_selector.css('span::text').get()
        date_string = arvdate_selector.re_first(r'\d{4}\.\d{2}\.\d{2}')  # 날짜 문자열 추출
        time_string = arvdate_selector.re_first(r'\d{2}:\d{2}:\d{2}')  # 시간 문자열 추출

        # 날짜와 시간을 datetime 객체로 변환
        date_time = datetime.strptime(f"{date_string} {time_string}", "%Y.%m.%d %H:%M:%S")
        formatted_date_time = date_time.strftime("%Y.%m.%d %H:%M:%S")

        # 본문을 추출한다
        # '#news_body_area' 내부의 모든 텍스트 노드를 선택
        context_nodes = response.css('#news_body_area ::text').getall()
        # 텍스트 노드에서 공백과 개행 문자를 제거
        cleaned_context = ''.join([text.strip() for text in context_nodes if text.strip()])

        print("제목: ", titles)
        print("부제목: ", subtitles)
        print("기자: ", journalist)
        print("날짜/시간: ", formatted_date_time)
        print("본문: ", cleaned_context)
        # print(response.body)      
