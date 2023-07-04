# Scrapy.md

## 0703 미리 작성해보기

1. Scrapy를 사용하는 이유.
- 크롤링 도구 중에 BeautifulSoup, Scrapy, Selenium가 데이터 파이프라인을 구축하는데 사용 될 수 있다.
- BeautifulSoup: BeautifulSoup는 HTML과 XML을 파싱하기 위한 간단하고 편리한 파이썬 라이브러리다. 그러나 BeautifulSoup 자체는 웹 페이지를 요청하거나 내려받는 기능을 갖고 있지 않으므로, 보통 requests와 같은 라이브러리와 함께 사용된다. BeautifulSoup는 단순하고 직관적이며, 상대적으로 쉽게 배울 수 있지만, 복잡한 웹 크롤링에는 한계가 있을 수 있다.

- Scrapy: Scrapy는 복잡한 웹 크롤링과 웹 스크레이핑 작업에 대한 강력한 프레임워크다. 병렬 처리, 요청 처리, 데이터 저장 등 많은 기능을 제공한다. Scrapy는 중대형 프로젝트나 복잡한 데이터 파이프라인에 적합하지만, 배우는 데 시간이 필요할 수 있다.

- Selenium: Selenium은 웹 페이지를 자동화하여 동작시키는 도구로서, JavaScript로 동적으로 로딩되는 웹페이지에서 데이터를 수집할 수 있는 장점이 있다. 그러나 실제 웹 브라우저를 실행하기 때문에 리소스를 많이 사용하고, 크롤링 속도도 느릴 수 있다.

따라서, 데이터 파이프라인을 구축하고 특정 신문사 웹사이트의 기사들을 크롤링하기 위해선, 보통 Scrapy가 좀 더 적합한 편이다.

Scrapy는 복잡한 웹 크롤링과 웹 스크레이핑 작업에 대한 강력한 프레임워크로, 복잡한 크롤링 작업과 병렬 처리, 데이터 저장 등 많은 기능을 제공합니다. 신문사의 웹사이트는 보통 많은 수의 기사와 페이지를 가지고 있으므로, 이런 크고 복잡한 작업을 자동화하고 관리하기 위해선 Scrapy가 더욱 적합하다.

scrapy는 javascript 지원이 힘들지만, 신문의 기사 정보를 가져오는데에 불필요 하므로 scrapy로 진행한다.

2. 공식문서
https://docs.scrapy.org/en/latest/index.html
를 참고하여 진행한다.

3. Scrapy 설치
pip install scrapy로, version 2.9.0을 설치했다.

4. 간단한 튜토리얼을 진행해서 다루는 법을 알아보자.
https://docs.scrapy.org/en/latest/intro/tutorial.html

    - 프로젝트 이름은 tutorial
        scrapy startproject tutorial 를 통해 프로젝트를 생성했다.
    - quotes_spider.py를 작성했고,
    - 프로젝트 최상위 directory(tutorial)에서 scrapy crawl quotes로 실행한다.
    - quotes-1.html 과 quotes-2.html이 생성되었다.

    - 데이터 추출

5. 데이터 추출 연습
    - test_spider.py를 이용하여 연습해보도록 한다.
    - http://www.newsprime.co.kr/news/article/?no=605756 의 class가 title, subtitle인 부분을 가져와 보도록 한다.


### 0704
1. 데이터 추출
    - url을 이용해서 제목, 소제목, 기자이름, 게시일, 본문 내용까지 추출하는데 성공했다.
    - mysql을 이용해서 저장하는 것을 해보도록 하자.

2. data 저장
    - mysql로 저장할 것은 정해졌으나, rds를 사용할 수 도 있고,, 일단 로컬에 저장할 것인지, 어떤 계정의 rds를 사용할 것인지 정해진 바가 없기 때문에
    - 차후 키워드 추출 작업을 위해 일단 csv 형태로 저장하기로 했다.

3. crawl_newsprime 프로젝트
    - crawl_newsprime 이라는 프로젝트를 생성했다.
    scrapy crawl num -a article_num=605756 와 같이 article num을 입력받아서 재활용 할 수 있는 구조로 만들었다.

    = starter.py라는 파일을 만들어서, article num을 외부에서 입력 받아서 실행시킬 수 있는 구조로 만들었다.


    

