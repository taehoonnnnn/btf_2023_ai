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
    - pandas 설치(2.0.3)
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
    - output.csv와 url.csv를 비교하여 새로운 기사만 크롤링 하도록 starter.py를 수정했다.
    - 다만 75개의 기사를 크롤링 하는데에 117초가 걸린 것은 시간이 과다하게 소모되므로 시간 절약을 위한 수단을 강구할 필요가 있다.
    - Scrapy 설정에서 CONCURRENT_REQUESTS 매개 변수를 늘려 동시에 처리할 수 있는 요청의 수를 늘리는 방법 또는 여러 스파이더를 동시에 실행하여 병렬 처리하는 방법을 시도해 보도록 하자.
    - CONCURRENT_REQUESTS 매개 변수를 늘리는 방법은 효과가 없었다.
    - 스파이더를 병렬 실행했을 때는, 크롤링이 제대로 되지 않은건지 저장이 되지 않았다.
    - ThreadPoolExecutor를 이용하여 여러 개의 스파이더를 동시에 실행시키는 방법으로 117초에서 34초로 줄였다.

4. crawl article number
    - beautiful soup와 scrapy에서는 1분이내 접근 횟수 오류가 계속 발생했지만, selenium은 가능했다. selenium으로 접근하기로 했다.
    - 현재 작업하는 pc에 차단이 걸린 듯하다.
    - 기사 리스트에서 url을 가져오는 것은 이 pc에서 beautifulsoup, scrapy, selenium의 사용여부와 관계없이 1분이내 접근 횟수 오류가 발생했고, url을 가지고 기사 내용을 크롤링 하는것은 가능했다.
    - url은 현욱님이 진행해주시기로 했고, 받아온 url을 가지고 크롤링 하기로 했다.

### 0707
1. 프로젝트 구체화
    - 데이터 수집에 기능은 대부분 구현되었다. url을 가져오는 기능은 모두 구현 되었고, 크롤링을 진행하기만 하면 된다.
    - 프로젝트 구체화를 통해, 차후 일정관리, 중간마감 설정, 담당업무 분배, 프로젝트 결과물을 통한 기대효과 등을 정리하기로 했다.
    - 기존에 사용하는 3c4p에서 3c에 가능한 많은 정보를 수집하고, 회의가 필요하다. (https://docs.google.com/document/d/1FM-Hxgfnz6L51S7quIKrquttcuz5Fmipn0b2JZWA98g/edit?usp=sharing)

2. 아이디어 회의
    - 프로젝트의 결과물을 어떤 것을 목표로 하고, 어떤 방식으로 구현할 수 있을지, 시장조사와 기대효과를 고려하여 아이디어 회의를 진행했다.
    - 기본 조건은 다음과 같다.
        1. 프라임 경제의 뉴스를 활용한다.
        2. 뉴스를 가공하여 소비자에게 유익한 형태로 축약, 정제한다

    - 여러가지 아이디어가 나왔으나, 추린결과
        1. bing과 같이 챗봇 형식으로 구성하여, 경제신문을 읽기 편하게 도와준다.
        2. 퀴즈형식으로 제시하여 뉴스 유입을 할 수 있도록 한다.
        3. 주식관련 뉴스를을 모아서 해당 주가 변동에 따라 추천 뉴스를 표기한다.
        4. 버튜버 형식으로 만들어서 뉴스를 읽어주고, 시청자와 대화를 나눈다.
        5. 카드뉴스를 자동생성하여 카톡으로 전달한다.
        6. 뉴스 축약 후 TTS로 읽어주는, 라디오 형식의 뉴스를 전달한다.
        7. 최신 뉴스 기반으로 관련 주 기사를 추천한다.
        8. 키워드, 분야별 분류와 추천으로 관심사만 기사만 제공한다.

    - 중에, 4번을 할 수 있는지 조사해보도록 했다. 4번을 할 수 있다면, 도중에 6번이 자연스럽게 구현될 것이라 기대한다.

3. crawling
    - 자본시장- 금융 크롤링 진행중, 2000개에, 15분 정도 소요됨.
    - output.csv가 없으면 자동으로 생성하도록 starter.py수정
    
### 0710
1. crawling
    - 현욱님과 누리님이 파트를 나눠서 url 크롤링중이며,
    - 이를 csv형태로 받아서 기사 내용을 크롤링중이다.
    - 마찬가지로 csv형태로 저장한다.
    - 크롤링을 진행하면서, 다른 작업에 착수하도록 한다.
    - 크롤링 결과물에 줄바꿈 문제가 있어 수정, '\r\n'과 '\n'을 제거했다.


2. summary
    - 핵심 기능인 summary는 naver clova summary에서 api 형태로 무료 제공하고 있다.(https://www.ncloud.com/product/aiService/clovaSummary)
    - 이 api를 사용하지 않기 때문에, 차별화되는 장점이나 특징이 있어야 한다.
    - clova summary의 특징은 
        1. 글자수가 2000자로 제한되어 있다는 점.
        2. 하루 1000회까지만 무료라는 점.
        이다.
    - 김태훈 팀장님의 가이드에 따르면
        1. 기사 몇개를 선정해서 GPT 3.5 or 4.0한테 요약해달라고 일정한 규칙을 붙여 요청 > 동일한 형태로 아웃풋데이터
        2. 를 위한 프롬포터 만들기
        3. '일정한' 데이터를 얻어야한다는 점을 유의.

    - chat gpt api를 사용하여 summary 해야하기 때문에 document을 찾아봤다.
    - https://platform.openai.com/docs/guides/gpt/chat-completions-api
    - https://platform.openai.com/docs/api-reference/chat/create
    - 관련 내용은 summafy 폴더의 readme에 작성한다.


3. keyword
    - summary와 마찬가지로 방법론에 대해 찾아보고, 진행하기로 했다.

    

### 0711   
1. summary, keyword
    - 수집 데이터 기반 뉴스 축약과 키워드 추출을 진행한다. 
    - 관련 내용은 summafy 폴더의 readme에 작성한다.
2. 평가방식
    - gpt api의 여러 모델과 피라미터 조정을 통해 테스트를 진행해야 하는데, 정량적 방법으로는 성능의 평가를 하기 어렵다.
    - 정성적 평가를 위해 적합한 자연어처리 평가 방식을 찾아봐야 한다.
        1. BLEU: 가장 보편적으로 사용되는 자연어처리 평가방식이지만, reference length와 output lenth의 비교를 통해 정확도를 측정하기 때문에 reference length가 없기 때문에 일단 보류한다.
        2. SSA: sensibleness와 speccificity의 두가지 항목으로 평가한다. 합리적인지와 구체적인지를 평가할 수 있다.
        3. LAMBADA dataset: 언어 모델의 이해력과 문맥 이해력을 평가하는 데 사용되는 데이터셋이다. "LAMBADA"는 "LAnguage Modeling BAbi and Discourse Abilities"의 약자로, 복잡한 문맥에서 단어를 예측하는 능력을 테스트하는 데이터셋이다. 이를 통해 모델이 긴 문장 또는 문단에 걸친 문맥을 얼마나 잘 이해하는지 평가한다.
        4. StoryCloze: gpt의 평가 방법 중 하나이지만, 후속 이야기를 추측하는데 쓰이는 지표이므로 적합하지 않다.
        5. HellaSwag: gpt의 평가 방법 중 하나이지만, 주어진 단어의 의미를 파악하고 다른 문장에서 쓰일 수 있는지 측정하는데 쓰이는 지표이므로 적합하지 않다.
        6. ROUGE-N: ROUGE-N은 요약문과 원문 사이의 N-gram 일치를 측정한다. 축약에서 많이 사용하는 평가지표이지만, 사람이 만든 참조 요약과 비교하는 방식으로, 일단 보류한다.

    - 우선, ssa와 lambada을 이용해 볼 수 있겠다.

    - ai hub에 있는 요약 데이터셋을 이용하여 성능 측정을 해볼 수 있겠다.
    (https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=582)

3. .env
    - 회사계정을 지원받아 api를 테스트해보기로 했다.
    - .env 파일 만들어서 소스파일에 덧대는 방식으로 구성하여 깃헙에 올라가지 않도록 설정한다.
    - python-dotenv 1.0.0을 이용한다.
    - .gitignore에도 .env를 추가한다.









    

