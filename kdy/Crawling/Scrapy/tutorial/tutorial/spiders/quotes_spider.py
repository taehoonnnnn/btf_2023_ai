from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    # name = spider를 식별한다. 다른 spider에 대한 동일한 이름을 설정할 수 없다.
    name = "quotes"

    # spider가 크롤링을 시작할 iterable requests를 반환해야 한다.
    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # 각 요청에 대해 다운로드 된 응답을 처리하기 위해 호출되는 메서드
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")