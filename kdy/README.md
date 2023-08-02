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
        1. 요약문 및 레포트 생성 데이터(https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=582)
        2. 문서요약 텍스트(https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=97)

3. .env
    - 회사계정을 지원받아 api를 테스트해보기로 했다.
    - .env 파일 만들어서 소스파일에 덧대는 방식으로 구성하여 깃헙에 올라가지 않도록 설정한다.
    - python-dotenv 1.0.0을 이용한다.
    - .gitignore에도 .env를 추가한다.

4. openai
    - openai 0.27.8 을 설치하고 진행한다.
    
### 0712
1. summary
    - 요약에 사용할 모델과 프롬포트에 따라 성능이 어떻게 달라지는지 측정할 것이다.
    - 성능평가에 사용하기 편하도록 aihub에서 받은 자료에서 기사 부분만 추출하고, json 형식을 csv형식으로 바꾼다.

    - 요약문 및 레포트 생성 데이터
        - 1. Training > 라벨링데이터 > TS1 > 01.news_r > 2~3sent의 각 파일에서 doc_name = 기사제목, passage = 본문, summary1 = 요약 1줄, summary2 = 요약 3줄, author= 기자, 게시시간 없음, publisher_year = 게시년도, 분야 없음
        - 2. Training > 라벨링데이터 > TS1 > 01.news_r > 20per의 각 파일에서
        doc_name = 기사제목, passage = 본문, summary1 = 요약 1줄, summary3 = 요약 3줄

        >> 차이점을 느끼기 어려움
    - 문서요약 텍스트
        - documents > media_sub_type = 경제지 여부, title = 제목, text > sentence = 본문, category = 분야, 기자 없음, publish_date = 게시시간
        +(text > index = 문장 순서)

    - pandas 2.0.3, numpy 1.25.1, pytz 2023.3, tzdata-2023.3를 추가 설치하고 진행한다.


2. openai api
    - summary > model 폴더를 만들어서 모델과 프롬포트를 수정하면서 테스트를 해볼 수 있도록 openai_api.py를 생성하였다.
    - 동시에 기존의 요약본과 간단히 비교하여 성능을 측정하기 위해 data1_val_23cent.csv에서 본문과 요약문을 가져오고, api를 통한 요약문을 합쳐서 csv형태로 저장하도록 test3.py를 작성하였다.

3. bleu score
    - 요약이 얼마나 잘 됐는지 정량적으로 평가하기 위해 자연어 처리에서 가장 많이 이용되는 bleu score를 시도해보자. bleu이외에 많은 평가방법이 있기 때문에 차후 다양한 평가로 전환한다.

    - 이를 위해 nltk-3.8.1 를 설치했다.

    - output.csv에서 각 행을 추출하고, 행마다의 bleu score를 구한 뒤, 평균 bleu를 구할 수 있도록 하는 cal_bleuscore.py를 작성했다.

### 0713
1. bleu score
    - bleu score는생성된 문장과 참조할 문장(Human generated) 사이의 얼마나 많은 n-grams가 겹치는지에 대한 precision의 기하평균으로 정의된다.
    - precision으로 정의되기 때문에 짧은 문장일수록 점수를 높게 받는 경향이 있으며, 이를 보정하기 위해 문장 길이에 advantage를 주는 (짧을 수록 penalty를 주는) Brevity Penalty를 적용한다.  
    - 단어의 순서를 고려하지 않는 문제점 보완되어 있고, 짧은 문장일수록 score가 높아지는 문제점도 보완 되어 있다. 
    - 다만, 같은 의미의 다른 단어여도 다른 단어를 쓰면 틀렸다고 판단하는 경향이 있다.

    다른 평가지표로 sacreBLEU, CHRF score, TER score, BLEURT등을 사용해 볼 수 있다.

2. scareBLEU
    - bleu의 BLEU Metric은 Tokenization을 어떻게 하느냐에 따라서 크게 달라지므로 현재 Machine Translation 에서는 NLTK 의 BLEU를 사용하지 않는다는 단점을 개선시켜 현재 bleu의 표준이라고 말해도 될 정도로 많이 사용되고 있다.
    - 아직 미구현

3. BLEULT
    - 사전 학습한 BERT를 Human Evaluation으로 Fine-tuning 하여 Human Evaluation을 훌륭하게 모델링한 Metric으로 sacreBLEU와 같이 많이 사용되고 있다.
    - 아직 미구현

4. calculate score
    - data1_val_23cent.csv에 open ai를 통해 받은 정보들이 csv형태로 정리되어 있으며,
    - create_output.py 를 통해 csv를 읽어서 비교할 '원문'과 '요약문'을 추출해 output.csv로 저장한다.
    - cal_bleuscore.py는 output.csv의 첫 열과 두 번째 열의 값을 가지고 bleucore를 계산한다.
    
5. output.csv 파일에 조건에 따라 열별로 본문/요약문1/요약문2/요약문3... 의 구조로 만들어서 비교한다?



### 0714
1. keyworld
    - 오늘부터 키워드 추출 작업을 시작하기로 했다.
    - 분야별로 다른 프롬포트를 사용할 예정이므로, 일단 자본시장 - 금융 부터 작업하도록 한다.
    - 많이나오는 단어, 기사의 주제, 기사의 핵심인물(또는 기업)을 키워드로 하며,
    - 카드뉴스는 제외하도록 한다.

    - 비용 측면에서 gpt-4는 gpt-3.5의 20배 정도의 가격이므로, gpt-3.5터보로 진행한다.
    - 월 100달러 까지 허용되어 있으며,
    - 사용량에 따른 청구금액을 중간 보고하면서 프로젝트를 진행하기로 했다.

    - 우선적으로 프라임경제 자본시장 - 금융 100개의 기사에 대한 키워드를 추출하고
    - 키워드와 openai api를 통해 요약한 문장 사이의 유사도에 대한 점수를 측정하여
    - 정량적, 정성적으로 얼마나 성능이 나오고, 개선이 필요한지 확인하도록 한다.

    - 기존에 크롤링 한 정보에서 키워드를 추가하는 작업이고, 동시에 작업해야 하므로 공유문서를 사용한다.(https://docs.google.com/spreadsheets/d/1oczjEF-vg6kxSNyEnSaOggkmcH0aV7HtASU_HQv1TbY/edit?usp=sharing)

    - 100개의 기사에 대한 키워드를 사람에 의해 5개씩 선정하였다. 이를 기준으로 요약문과의 유사도를 검증할 예정이다. 
    - 이는 scrapy > crawl_newprime > keyword 폴더에 저장한다.

### 0717
1. data
    - 14일 진행했던 파일을 팀장님이 확인하고 데이터형식을 다시 지정해주신다고 한다.
    - 이를 바탕으로 수정한다.
        1. kewyword는 각각 column을 차지하도록 수정한다.
        2. 게시일은 년,월,일로 수정한다.
        3. mysql을 이용하여 db화 하기 전에 ,를 다른 문자로 변환하여 치환하여야 한다. 이는 차후 진행한다.
        4. "[프라임경제]"는 불필요한 정보이므로 content에서 생략한다.


### 0718
1. summary & score
    - 파라미터의 변화에 따른 score를 그래프로 그리는 것 까지를 목표로 하며
    - 이를 위해서 해야할 작업은 
        1. article_number, message, response, score, model, temperature, max_tokens, top_p, frequency_penalty, presence_panalty를 column으로 가지는 dataframe만들기
        2. score의 계산방식은 추출한 키워드를 요약문에서 얼마나 잘 반영하고 있는지 count하여 계산한다.
        3. score에 관련한 부분은 차후 수정할 수 있으므로 함수 형식으로 제작한다
        4. 최적화까지 자동으로 할 수 있다면 인력 소모를 줄일 수 있겠으나, 현재 토큰에 대한 비용문제로(월 100달러) 가능한 시도 횟수를 줄여야하기 때문에, 수작업으로 진행한다.
        5. 그래프는 파라미터 조건이 많으므로, 조건을 표 형식으로 제시한다
        6. 제목을 포함했을 때, 제목을 포함하지 않았을 때의 그래프를 따로 그린다.


2. openai api error
    - openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens. However, your messages resulted in 4464 tokens. Please reduce the length of the messages.
    라는 오류가 606050 기사에서 계속 발생하는데
    토크나이저 계산기에 넣어보면 2000토큰도 되지 않는다.

    - openai.error.ServiceUnavailableError: The server is overloaded or not ready yet.
    - bad gateway{"error::{"code":502, "message":"bad gatway}}...


### 0719
1. score
    - openai_api.py를 이용하여 요약문을 생성하고 output.csv로 저장한다.
    - add_score.py를 이용하여 score를 계산하고 output2.csv로 저장한다
    - cal_score_maen.py를 이용하여 score의 평균을 계산하고 print한다.

    

2. token
    - openai.error.ServiceUnavailavleError: The server is overloaded or not ready yet.
    - openai의 api는 분당 요청횟수, 하루 요청횟수, 분당 토큰 횟수가 제한되어 있다.(https://platform.openai.com/docs/guides/rate-limits/overview)
    - 분당 토큰 횟수를 초과해 오류가 나는 것으로 보이며, 이를 줄일 수 있는 방법으로
        1. 한국어 content > 영어 번역 > openai api > 영어 summary 도출 > 한국어 번역
            의 방법을 사용할 수 있다.
            이 방법은 기존 대비 20%로 토큰 수를 줄일 수 있지만,
            키워드 중심의 평가방식에서 다소 불리할 것으로 보이며
            특히 고유명사를 번역하는데 있어 불리하다.

            papago api를 활용하는 translate.py를 만들었으나, 
            urllib.error.HTTPError: HTTP Error 429: Too Many Requests 에러가 발생하였고, 찾아보니 파파고 API에서 무료로 제공하는 일일허용량이 1만자로 제한되어있었다. 

            구글 번역기도 1일 1만자, 카카오의 경우 1일 5만자 까지 제공한다.

            selenium을 이용하는 방법으로 시도해본다.

        2. 번역 이외의 방법
            - 자본시장_금융의 content 평균 길이는 1167자이며, 약 2200토큰이다.
            - 영어로 번역할 경우 평균 길이는 2164자이며, 약 450토큰이다.
            - 문서 분할, 핵심 부분 추출, 
    

    여러가지 방법을 찾아봤는데,
    1. 한국어 > 영어 번역을 통해 토큰수를 줄인다. 
        - papago의 유료계정을 이용하거나
        - selenium을 이용할 수 있다.
        - content와 keyword를 번역하고 summary와 keyword를 비교하여 score를 계산한다.
        이때 사용한 프롬포트를 다시 한국어 버전에서 사용할 것인지, 차후 한국어로 다시 번역할 것인지는 테스트해보도록 한다.
    2. 문서 분할 방법
        - 문서 분할 방법은 오히려 1회당 토큰 수는 줄어들지만, 1일 토큰 사용량이 늘어나게 되므로 실질적 사용에 메리트는 적다.
    3. 문서 요약 방법
        - 이 방법은 다른 자연어 처리 모델을 활용하여(bart등) 요약문을 생성한 뒤, 다시 요약을 하는 방법으로, 효용성있는 방법이나 하이퍼파라미터 조정이나 학습에 시간이 걸리는점, colab으로는 비용이 너무 많이 든다는 점, 사용가능한 gpu가 1대라는 점이 발목을 잡는다.
    4. autogpt 활용 방법
        - 프롬포트를 스스로 생성하는 autogpt가 프롬포트를 찾아주는데에 도움이 될 것으로 추측된다. 비용과 효과면에서 추가적인 조사가 필요하다.
    
### 0720
1. 평가방법
    -  다양한 조건에서 0점에서 5점까지 다양하게 분포되어 있다. 
    - 0점인 경우에는 키워드가 합성어로 되어있는 경우가 많았고, 5점인 경우에는 키워드가 단일어로 되어있는 경우가 많았다. 
    - 하지만 0점인 경우에도 각 요약문에 키워드와 동일하거나 비슷한 의미의 단어들이 사용되었고, 이를 정확히 평가하지 못한 것으로 보인다. 
    - 추가적으로 요약문 또한 기존의 기사에서 내용이 벗어나지 않았다.
    - 이를 감안할 때, 키워드와 유사한 경우에도 평가할 수 있는 평가방법이 필요하다고 여겨진다.
    - 따라서 이를 보완한 평가방법이 필요하며 이를 조사하고 구현해보기로 했다.
    1. 키워드를 늘리는 방법
    2. 키워드에 특정 문자가 맞을시에 통과되는 방법
    을 사용할 수 있고,

    -TF-IDF 계산, Word Embedding 적용, Cosine Similarity 계산을 통해 유사도 점수를 기반으로 문장과 키워드 간의 최종 유사도 점수를 구할 수 있다.

2. TF-IDF와 코사인 유사도
    - pip install scikit-learn을 통해 scikit-learn-1.3.0 scipy-1.11.1 threadpoolctl-3.2.0을 설치하였다.
    - 형태소 분석을 하지 않으면 의미 있는 단어로 분리할 수 없고, tf-idf계산에 이는 필수적이다.

3. 평가방법
    - 단어 임베딩 방법 중 하나인 Sentence-BERT(SBERT)를 사용하여 문장과 키워드 간의 유사도를 계산하는 방법
    -  SBERT는 BERT를 기반으로 문장 임베딩을 생성하며, 이를 통해 문장 간의 유사도를 계산할 수 있다.

    - sentence-BERT는 문장 간의 유사성을 계산하는 데 특화되어 있다. BERT 모델은 개별 토큰에 대한 벡터를 생성하지만, Sentence-BERT는 전체 문장에 대한 벡터를 생성한다.
    - GloVe는 Co-occurrence 통계에 기반한 단어 임베딩 기법으로, 문맥을 고려하여 단어의 의미를 임베딩하지만, GloVe는 문장 전체의 의미를 포착하는 데는 제한적이다.
    - FastText는 각 단어를 n-gram의 집합으로 취급하여 임베딩을 생성한다. 오탈자나 다른 형태의 단어도 적절하게 처리할 수 있다. 문장 전체의 의미를 포착하는 데는 제한적이다.
    - ELMO는 문맥에 따라 단어의 임베딩을 동적으로 생성하는 딥 러닝 모델로, 단어의 문맥에 따른 다양한 의미를 잘 포착할 수 있다.
    - USE는 문장 전체를 고려하여 임베딩을 생성합니다. 이 모델은 여러 언어를 지원하며, 크기가 작은 두 가지 버전 (DAN과 Transformer)이 있다.
    - Word2Vec을 기반으로 하는 Doc2Vec은 문장이나 문서 전체의 임베딩을 생성한다.
    - InferSent는 문장의 임베딩을 생성한다. 이 모델은 Supervised Learning 방식으로 학습되며, 특히 감정 분석 등의 작업에서 좋은 성능을 보인다.

    - 다음은 USE, InferSent, Doc2Vec을 시도해보도록 하자.

    - SBERT
        - pip install sentence_transformers를 통해 sentence_transformers-2.2.2 torch-2.0.1 torchvision-0.15.2 transformers-4.31.0를 설치했다.
        - setence BERT를 이용한 평가는 sentenceBERT.py를 통해 구현했다.

    - USE
        -pip install absl-py를 통해 absl-py-1.4.0를 설치했다.
        -pip install tensorflow를 통해 astunparse-1.6.3 cachetools-5.3.1 flatbuffers-23.5.26 gast-0.4.0 google-auth-2.22.0 google-auth-oauthlib-1.0.0 google-pasta-0.2.0 grpcio-1.56.2 h5py-3.9.0 keras-2.13.1 libclang-16.0.6 markdown-3.4.3 numpy-1.24.3 oauthlib-3.2.2 opt-einsum-3.3.0 protobuf-4.23.4 requests-oauthlib-1.3.1 rsa-4.9 tensorboard-2.13.0 tensorboard-data-server-0.7.1 tensorflow-2.13.0 tensorflow-estimator-2.13.0 tensorflow-intel-2.13.0 tensorflow-io-gcs-filesystem-0.31.0 termcolor-2.3.0 typing-extensions-4.5.0 urllib3-1.26.16 werkzeug-2.3.6 wheel-0.40.0 wrapt-1.15.0를 설치했다.
        -pip install tensolflow-hub를 통해  tensorflow_hub-0.14.0를 설치했다.

### 0721

  1. score
    - 지금까지 구축한 평가 방법은 아래와 같다.
    - 키워드 기반 평가
        - 키워드가 요약문에 포함되어 있는지 여부를 확인하고, 포함된 갯수를 점수로 한다.(0~5점)
    - 모델 기반 평가: content와 summary를 벡터화하여 문장 간의 코사인 유사도를 측정하여 점수로 한다.
        - SBERT: sentence-BERT라는 문장간 유사도를 계산하는데 특화되어 있는 모델을 사용한다.(0~100점)
        - USE: SBERT와 유사한 Universal Sentence Encoder를 사용한다. (0~100점)

    - 한국어 그대로 평가한 경우와, 영어로 번역해서 평가한 경우의 점수는 아래와 같다.
        eng default
        keyword_eng 1.72
        SBERT 0.83
        USE 0.746
        fasttext 0.97

        kor default
        keyword 2.92
        SBERT 0.754
        USE 0.581
        fasttext 0.889
        kobert 0.868
        koelectra 0.891


  2. Glove
    pip install gensim을 통해 gensim-4.3.1 smart-open-6.3.0을 설치했다.
    영어 기반이기 때문에, 한국어의 유사도는 검증할 수 없다.

  3. fasttext
    모델을 다운로드 받았다. 약 6.7기가바이트 정도의 크기이기 때문에, .gitignore를 통해 git에 업로드 되지 않도록 하였다.
    fasttext.py를 통해 구현했다.

  4. kobert
    kobert.py를 통해 구현했다. 보강 작업이 필요하다.

  5. koelectra
    koelectra.py를 통해 구현했다. 보강 작업이 필요하다.
  

  6. database화 준비
    - 미리 HeidiSQL 12.5을 설치했다.

  7. 평가방식의 오류가 있었다. 다시 검증할 것.

### 0724
  1. Glove
    - gloeve.6B.300d를 사용하였다.
    - eng default기준 0.969의 점수가 나왔다.
    - gitignore에 glove.6B.300d.word2vec.txt를 추가했다.

    - 한국어 그대로 평가한 경우와, 영어로 번역해서 평가한 경우의 점수는 아래와 같다.
        eng default(output.csv)
        keyword_eng 1.72
        SBERT 0.83
        USE 0.746
        fasttext 0.97
        glove 0.969

        kor default(output_kor.csv)
        keyword 2.92
        SBERT 0.754
        USE 0.581
        fasttext 0.889
        kobert 0.868
        koelectra 0.891


  2. kor 폴더와 eng 폴더로 평가방식을 구분하였고,
    score_kor.py와 score_eng.py를 이용해 각각의 평가로 score를 추출한 뒤,
    cal_score_mean.py를 통해 averages.csv에 평가항목들이 저장되도록 수정하였다.


  3. 한국어, 영어, 번역
    한국어 기본값으로 설정했을 때와, 한국어에서 영어로 번역후 api를 돌리고 한국어로 다시 번역했을 때의 성능에 미묘한 차이는 있지만 그 경향이 바뀌지 않아서 토큰의 차이가 5배라는 점을 고려하면 영어로 번역해서 사용해도 될 것 같다,
    다만, 키워드같은 경우에는 점수차이가 비교적 크게 나타났다

  4. 키워드 평가 보완
    - 유사한국어 번역하는 오픈소스가 있을거같은데 
    - 저희 키워드에 특정 문자가 맞을시에 통과되게끔 하는 방법(감원의 문자를 단위로 쪼개서 배열화시키고 키워드도 배열화시켜서 문자가 포함되어있으면 통과되게끔 하는 형식 등의 방법)
    - GPT의 데이터를 보고 키워드 선택의 방향성을 잘 고려

### 0725
  1. 키워드 평가 보완
    - 어느부분에서 보완해야 할지 어렵기 때문에 한국어 자연어처리 기법을 조사했다.
    1. 형태소 분석 (Morphological Analysis): 형태소 분석기 KoNLPy가 주로 사용된다.
        - KoNLPy
    2. 의미 분석 (Semantic Analysis): 단어나 문장의 의미를 분석하는 과정, 일한 단어가 다른 맥락에서는 다른 의미를 가질 수 있다. 주변 단어와의 관계를 파악한다.
        - USE
    3. 단어 임베딩 (Word Embedding): 벡터로 표현한다. Word2Vec, GloVe, FastText
        - FastText
        - USE
    4. 트랜스포머 모델 (Transformer Models): BERT, GPT등의 트랜스포머 기반 모델 
        - SBERT
        - KoBERT
        - KoElectra

    - 1에 해당하는 방법으로 konlpy의 okt 형태소 분석기를 사용하였다.
    okt.py로 구현하였고, 금융감독원과 금감원이 동일어임을 이해하진 못했다. 
    - 이를 보완하기 위해 '금감원'에 '금융감독원'도 추가하였으나, {'은행권 연체율': 6, '금감원': 1, '금융감독원': 0, '기업 연체율': 5, '추세 유지': 1, '가계대출 연체율': 8} 와 같은 결과가 나왔다.

  2. score
    - 현욱님이 요약방법론 기반으로 작성한 
    output_Abstractive, output_cosine, output_Pointer-Generator_Networks,
    TextRank, TF-IDF, TSRL에 대하여 각 평가방법에 대한 점수를 추출하였다.


### 0726
  1. 요약방법론 기반 유의미한 점수변화가 나타나지 않는 문제에 대해서 회의
    1. 요약방법론이 잘못되었나?
        > 요약방법론을 사용하지 않고 temperature, top_p와 같은 파라미터의 변화에 따른 점수변화를 측정하여 검증합니다.
    2. 평가방식이 잘못되었나?
        > GPT4를 이용하여 요약한 요약문을 기존 방식으로 평가하고, 점수변화를 측정하여 검증합니다.
    3. GPT3.5가 너무 성능이 뛰어나기 때문인가?
        >  davinci와 같이 openai api의 다른 모델을 이용하여 요약한 요약문을 기존 방식으로 평가하고, 점수변화를 측정하여 검증합니다.

    추가적으로 영어로 된 요약문을 정성평가하는데 어려움이 있어, 요약문의 최대글자수, 최소글자수, 평균글자수, 분산을 측정하여 요약문의 성능을 평가하는 지표를 추가한다.

  2. 코드품질
    재사용성과 확장성을 높일 수 있도록 score.py score_eng.py cal_score_mean.py cal_score_mean_eng.py를 수정했다.

  3. graph
    데이터 분석과 시각화를 위해, 각 지표에 대한 평균, 최솟값, 최댓값, 표준편차를 구하였고
    이를 graph.py를 이용해 시각화 할수 있도록 구현하였다.
    이를 위해 seaborn을 설치했다.

### 0727
  1. score
    오류를 수정한 csv를 통해 다시 점수를 측정한다.
    - output.py(eng_default)
    - output_Abstractive..csv
    - output_cosine..csv
    - output_Pointer-Generator_Networks..csv
    - output_TextRank..csv
    - output_TF-IDF..csv
    - output_TSTL..csv
    의 점수를 우선 측정한다.

  2. score 비교
    - https://docs.google.com/presentation/d/1H9Bahq4ewFi3VKzGXP3c55vQpC1iNNJ1GzblY-CP9SE/edit?usp=sharing

    1. 요약방법론 기반 프롬포트에 따른 기사-요약문간 유사도는 거의 유사하다.

    2. 요약방법론 기반 프롬포트에 따른 기사-요약문간 요약문(respoonse)의 평균, 최소, 최대길이에는 유의미한 차이가 있었다.
    - pointer-generator_networks의 최댓값이 유난히 낮은 것
    - 이를 표준편차로 확인해 보면, pointer-generator-netwoks가 default에 비해 24.72% 낮은 것을 확인할 수 있다. 

    3. 모델에 따른(gpt-3.5 turbo, dacvinci 003) 기사-요약문간 유사도는 거의 유사하다.

  3. 가설 검증
    1. 요약방법론이 잘못되었나?
      > 요약방법론을 사용하지 않고 temperature, top_p와 같은 파라미터의 변화에 따른 점수변화를 측정하여 검증합니다.
      > 파라미터 변화에 따른 요약문 변화는 진행중이다.
      > 요약방법론의 점수와 요약문 길이를 비교해본 결과 Pointer-Generator_Networks에서 유의미한 수치변화가 나타났다.
    2. 평가방식이 잘못되었나?
      > GPT4를 이용하여 요약한 요약문을 기존 방식으로 평가하고, 점수변화를 측정하여 검증합니다.
      > GPT4 아직 사용 불가
    3. GPT3.5가 너무 성능이 뛰어나기 때문인가?
      >  davinci와 같이 openai api의 다른 모델을 이용하여 요약한 요약문을 기존 방식으로 평가하고, 점수변화를 측정하여 검증합니다.
      > davinci 003과 gpt3.5turbo의 성능은 거의 유사하게 측정된다.

  4. finetunning
    1. 미세 조정은 현재 기본 모델인 davinci, curie, babbage및 에만 사용할 수 있다.
    2. 이러한 모델은 2024년 1월 4일에 사용 중지된다. 
    3. GPT-4 및 GPT-3.5 Turbo에 대한 finetunning은 올해 말 공개될 예정이다.
    4. GPT-3.5 Turbo의 finetunning을 기다리는 방법과, 지난주에 오픈소스로 공개된 llama2를 이용하는 방법이 있다.

    
### 0728
  1. score
    모델기반, 오약방법론기반, 파라미터 기반 점수를 추출하고 그래프로 그린다.
    1. 모델기반
        gpt3.5 turbo
        davinci 003
    2. 요약방법론 기반
        abstractive
        cosine
        pointer-gererate-network
        textRank
        TF-IDF
        TSRL
    3. 파라미터기반
        temperature /  0, 1, 2
        top_p / 0, 0.4, 0.7, 1
        frequency penalty / -2, -1, 0, 1, 2
        presence penalty / -2, 0, 2
        max token / 

  2. graph
    histogram.py와 make_graph를 이용해 그래프를 그린다.


### 0731
  1. graph
    - 모델기반, 오약방법론 기반, 파라미터 기반 요약문에 대한 점수를 추출하고 그래프로 그렸다.
  2. db화
    - db는 내일 진행, erd도 그리긴 했으나, 내일 진행()

### 0801 
  1. db화
    - db와 erd관련 내용은 내일 진행하기로 했다.
  2. 자동화
    - db가 준비된 다음에 진행할 수 있다.
  3. kor default, eng default, aihub data의 비교
    - 평균 점수, 밀도를 그래프로 그려서 시각화 했다.
    - ai hub의 요약문이 보다 균일한 점수를 보이는 것을 확인할 수 있었다.
    - 이는 https://docs.google.com/presentation/d/1H9Bahq4ewFi3VKzGXP3c55vQpC1iNNJ1GzblY-CP9SE/edit?usp=sharing
    에 정리되었다.
    - role과 가이드라인을 제시한 방법의 점수를 측정하고 평가하였다.
    - 평균점수에는 유의미한 변화를 발견할 수 없었지만, 그래프의 양상변화는 눈에 띄었으며
    - 이를 통해 특정 점수 이상의 갯수가 몇 개인지 확인하는 등의 평가방법이 필요하다고 판단된다.

### 0802
  1. 회의
    - erd와 db관련 회의를 진행했다.
    - article_num, title, content, reporter, article_date, class, subclass, summary로 table의 column을 정했다.
    - 최근 1년간의 기사들에 대한 요약문을 생성하고, 전달하기로 했다.
    - 내부 table과 외부 table을 구성하여 용도에 따라 구분하기로 했다.
    - 어떤 형식의 서비스를 구현할 것인가에 대해서는 차후 다시 논의하기로 했다.
    - 이에 따른 시장조사가 필요하다.

  2. 프롬프트
    - 크롤링 > db > 번역 > db > api > db의 data흐름에서 필요한 프롬프트를 설정할 필요가 있다.
    - 평균 점수가 가장 높게 나오는 영어 default로 일단 사용하기로 했다.

  3. 크롤링
    - 기존에 크롤링해서 모아뒀던 url을 가지고 기사의 article_num, title, content, reporter, article_date, class, subclass, summary에 대한 정보를 수집하여 db에 저장하는 작업을 진행한다.

  4. 444



    

