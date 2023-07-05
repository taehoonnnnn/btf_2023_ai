import scrapy
import csv
from datetime import datetime
import os.path

class MySpider(scrapy.Spider):
    name = 'article'

    def __init__(self, article_num, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        global article_num_str
        article_num_str = str(article_num)
        self.start_urls = ['http://www.newsprime.co.kr/news/article/?no=' + str(article_num)]
        self.csv_file = 'output.csv'
        self.csv_exists = os.path.isfile(self.csv_file)  # 기존 CSV 파일이 있는지 확인

    def start_requests(self):
        # CSV 파일이 존재하면 추가 작성 모드로 열기, 존재하지 않으면 새로 생성
        mode = 'a' if self.csv_exists else 'w'
        with open(self.csv_file, mode, newline='', encoding='utf-8-sig') as file:
            self.csv_writer = csv.writer(file)
            if not self.csv_exists:
                self.csv_writer.writerow(['Article number', 'Title', 'Journalist', 'Date/Time', 'Content'])
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        titles = response.css('.title::text').get()
        # subtitles = response.css('.subtitle::text').get()
        arvdate = response.css('.arvdate').get()
        arvdate_selector = scrapy.Selector(text=arvdate)
        journalist = arvdate_selector.css('span::text').get()
        date_string = arvdate_selector.re_first(r'\d{4}\.\d{2}\.\d{2}')
        time_string = arvdate_selector.re_first(r'\d{2}:\d{2}:\d{2}')
        date_time = datetime.strptime(f"{date_string} {time_string}", "%Y.%m.%d %H:%M:%S")
        formatted_date_time = date_time.strftime("%Y.%m.%d %H:%M:%S")
        context_nodes = response.css('#news_body_area ::text').getall()
        cleaned_context = ''.join([text.strip() for text in context_nodes if text.strip()])

        with open(self.csv_file, 'a', newline='', encoding='utf-8-sig') as file:
            self.csv_writer = csv.writer(file)
            self.csv_writer.writerow([article_num_str, titles, journalist, formatted_date_time, cleaned_context])

        # print("제목: ", titles)
        # print("부제목: ", subtitles)
        # print("기자: ", journalist)
        # print("날짜/시간: ", formatted_date_time)
        # print("본문: ", cleaned_context)

    def close(self, reason):
        pass
