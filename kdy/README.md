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
    - starter.py를 만들어서, 위의 명령어를 함수로 만들어서 실행시킬 수 있도록 만들었다.
    - 다음은 크롤링할 article num의 리스트가 필요하다.

2. article num 크롤링
    - get_article_number 프로젝트를 생성했다.
    - 예를들어, http://www.newsprime.co.kr/news/section_list_all/?sec_no=66&page=2의 class="news1"인 부분의 a 태그의 주소를 읽어와야 한다.









    

