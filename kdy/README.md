# BTF Tech 
### 0703
0. 목표
    - 프라임 경제의 카테고리별 크롤링 진행(http://www.newsprime.co.kr/) 

1. 개발환경 설정
    - 파이썬 사전 설치(python 3.10.11)
    - vscode 설치(version 1.79), markdown editor 설치
    - git 설치(git version 2.41.0.windows.1)
    - mysql 설치(MySQL Community Server 8.0.33)
    - 가상환경 설정
    
2. 가상환경
    - 가상환경 이름 venv
    - pip version 23.1.2
    - beautifulsoup4 설치(version 4.12.2)
    - requests 설치(version 22.31.0)
    - scrapy 설치(version 2.9.0)
    - selenium 설치(version 4.10.0)
    - requirements.txt 생성

3. git
    - 주소: https://github.com/boogleboogle/btf

4. crawling
    - 프라임 경제 홈페이지의 카테고리, url > Categories.md 참고
    - 자료구조 > 0704 안내받을 예정.

### 0704
0. 목표
    - 프로젝트 본격 시작, 목표 확인 및 data 수집

1. github 
    - https://github.com/taehoonnnnn/btf_2023_ai
    - 개인별 branch 작성하여 작업
    - kdy 폴더 생성 후 지금까지 작업한 내용 push

2. newsprime 
    - scrapy 폴더내에, crawl_newsprime 프로젝트 생성
    - readme에 따라 제목, 분야, 내용, 기자, 게시시간 을 db화 시키기로 했다.
    - 차후, 이 내용을 바탕으로 키워드를 생성하기로 했다.
    - db는 프로젝트에서 많이 사용되는 oracle과 mysql중에 프로젝트 단위에 더 적합한 mysql로 사용하기로 결정했다.


### 0705
0. 목표 
    - data 파이프라인 만들기를 위한 사전준비
    - 확인 결과 aws glue를 활용하는 것이 대표적이다. 
    - 워크플로를 작성하기는 차후에 진행하도록 하고, 우선적으로 db를 작성해보도록 하자.
    - db 구성을 위해 erd를 그려야 한다.
    - 시장조사가 필요하다.

1. 크롤링
    - 1차적으로 csv를 먼저 만들어서 차후 db화 시키기로 결정했다.
    - scrapy crawl num -a article_num=605932 와 같은 형식으로 실행하여 기사 번호를 받을 수 있도록 수정했다.
    - make_csv.py를 만들어서, 위의 명령어를 함수로 만들어서 실행시킬 수 있도록 만들었다.
    - 다음은 크롤링할 article num의 리스트가 필요하다.

2. article num 크롤링
    - get_number 프로젝트를 생성했다.
    - 예를들어, http://www.newsprime.co.kr/news/section_list_all/?sec_no=66&page=2의 class="news1"인 부분의 a 태그의 주소를 읽어와야 한다.
    - 해당 웹사이트에 1분당 접근 횟수가 제한되어 있다. 

3. 시장조사
    - 비슷한 서비스가 있는지, 어떤 기능과 효과를 얻고 있는지 확인이 필요하다
    - 국내사례
        - clova summary https://medium.com/naver-cloud-platform/%EC%9D%B4%EB%A0%87%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EC%84%B8%EC%9A%94-clova-summary%EB%A1%9C-%EB%89%B4%EC%8A%A4-%EC%9A%94%EC%95%BD-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EC%9D%B4%EA%B1%B4-%EB%A7%88%EC%B9%98-%EC%84%B8%EC%A4%84-%EC%9A%94%EC%95%BD-%EB%B4%87-dac29e97d1e4

        - 네이버 속보 요약 프로젝트 https://ai-creator.tistory.com/36
        - 연합뉴스 인공지능 요약 서비스 https://www.yna.co.kr/view/AKR20210111095300527
        - 네이버 보이스 뉴스 https://www.yna.co.kr/view/AKR20200731065600017
        - 네이버 요약봇 https://help.naver.com/service/5603/contents/18902?osType=PC&lang=ko
        - 다음 자동요약 https://0and24.tistory.com/entry/%EB%89%B4%EC%8A%A4-%EC%9A%94%EC%95%BD%ED%95%B4%EC%84%9C-%EB%B3%B4%EB%8A%94-%EB%B2%95
        - ai 기반 뉴스 요약 https://blog.est.ai/2021/06/news-summary/
        - summary tool https://summary-tool.com/kr
        - 인스타 창업자의 뉴스앱 아티팩트 https://www.digitaltoday.co.kr/news/articleView.html?idxno=474952
    - 해외사례
        - summary news https://www.summary.news/posts/subjects/all
        - oneai https://www.oneai.com/summarize

### 0706 
1. 프로젝트 방향성
    - 3c4p 분석 도구를 이용하여, 프로젝트의 방향성을 구체화 하기로 했다.
    - 이를 위해 구글 문서를 생성했다.(https://docs.google.com/document/d/1FM-Hxgfnz6L51S7quIKrquttcuz5Fmipn0b2JZWA98g/edit?usp=sharing)
    - 시장조사를 비롯한 내용들을 이 문서에 정리할 계획이다.

2. article number
    - 기사 번호를 추출하는데 있어, 기사 목록창에서 계속 접근 제한이 반환된다.
    - 응답코드는 200, scrapy라이브러리에 접근 횟수에 제한 기능이 기본설정되어 있지 않기 때문에 웹사이트에서 막은 것으로 예측된다.
    - 반환은 "1분이내 접근 횟수를 초과 하였습니다. 브라우저를 완전 종료후 다시 실해해 주세요."라고 나오는데, 다음 날 시도 했을 때도 같은 오류를 내는 것을 보아 딜레이 이외의 다른 접근방식이 필요하다고 생각된다.
    - 현욱님이 selenium으로 기사번호 추출을 시도하기로 했다.

3. crawl
    - 현욱님이 만든 url.csv를 바탕으로 starter.py를 통해 크롤링 할 수 있도록 수정했다.
    - url.csv에서 url을 읽고, article number를 추출하여 크롤링할 수 있다.
    - 다만 1개 기사에 1초 정도 걸리는 것은 시간이 과다하게 소모되므로 시간 절약을 위한 수단을 강구할 필요가 있다.
    - Scrapy 설정에서 CONCURRENT_REQUESTS 매개 변수를 늘려 동시에 처리할 수 있는 요청의 수를 늘리는 방법 또는 여러 스파이더를 동시에 실행하여 병렬 처리하는 방법을 시도해 보도록 하자.
    - output.csv와 url.csv를 비교하여 새로운 기사만 크롤링 하도록 starter.py를 수정했다.









    

