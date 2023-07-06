import subprocess
import csv
import re
import time
start = time.time()  # 시작시간을 저장한다.


# article_num을 입력받아 스파이더를 실행시키는 함수
def run_spider(article_num):
    command = f'scrapy crawl article -a article_num={article_num}'
    process = subprocess.Popen(command, shell=True)
    process.wait()


# url.csv의 url을 읽는다
with open('url.csv','r') as f:
    rdr = csv.reader(f)

    # 정규표현식을 사용하여 url로부터 article number를 추출하여 article_number_list에 저장한다.
    article_number_set = set()

    for line in rdr:
        match = re.search(r'no=(\d+)', line[1])
        if match:
            article_number = match.group(1)
            article_number_set.add(article_number)
        else:
            print("No match found")

# 점차 데이터의 양이 증가할 예정이기 때문에 성능상의 이유로 set으로 변경한다.
# output.csv에서 article number를 가져와, 그 값이 article_number_set에 있으면 set에서 제거한다.
with open('output.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    for line in rdr:
        article_number = line[0] # output.csv 파일에 따라서 수정이 필요할 수 있음.
        if article_number in article_number_set:
            article_number_set.remove(article_number)

# 수정된 article_number_set 기준으로 크롤링하여, 정보를 output.csv에 저장한다.
for i in article_number_set:
    run_spider(i)


print(time.time() - start) # 현재시각-시작시간 = 실행시간
