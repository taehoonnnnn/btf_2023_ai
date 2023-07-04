import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://www.newsprime.co.kr/news/article/?no=605756']

    def parse(self, response):
        titles = response.css('.title::text').getall()
        subtitles = response.css('.subtitle::text').getall()      
        # contexts = response.css('#news_body_area').getall()     
        # contexts = response.css('.smartOutput').getall() 

        # '#news_body_area' 내부의 모든 텍스트 노드를 선택
        context_nodes = response.css('#news_body_area ::text').getall()
        
        # 텍스트 노드에서 공백과 개행 문자를 제거
        cleaned_context = ''.join([text.strip() for text in context_nodes if text.strip()])

        print("제목: ", titles)
        print("부제목: ", subtitles)
        print("본문: ", cleaned_context)
      
