from scrapy.crawler import CrawlerProcess
from crawl_newsprime.spiders.article_number_spider import MySpider

# CrawlerProcess 인스턴스를 생성합니다.
process = CrawlerProcess()

# MySpider를 CrawlerProcess에 추가합니다.
process.crawl(MySpider, article_num=605756)  # 원하는 article_num을 전달합니다.

# 크롤러를 실행합니다.
process.start()