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
f = open('url.csv','r')
rdr = csv.reader(f)

# 정규표현식을 사용하여 url로부터 article number를 추출하여 article_number_list에 저장한다.
article_number_list = []

for line in rdr:
    match = re.search(r'no=(\d+)', line[1])
    if match:
        article_nuber = match.group(1)
        article_number_list.append(article_nuber)
    else:
        print("No match found")
 
f.close()
# article_number_list 기준으로 크롤링하여, 정보를 output.csv에 저장한다.
for i in article_number_list:
    run_spider(i)


print(time.time() - start) # 현재시각-시작시간 = 실행시간
