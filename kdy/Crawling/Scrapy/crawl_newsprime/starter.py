import os
import subprocess
import csv
import re
import time
from concurrent.futures import ThreadPoolExecutor

start = time.time()
input_name = '자본시장_금융.csv'

# article_num을 입력받아 스파이더를 실행시키는 함수
def run_spider(article_num):
    command = f'scrapy crawl article -a article_num={article_num}'
    process = subprocess.Popen(command, shell=True)
    process.wait()

# url.csv의 url을 읽는다
with open(input_name,'r') as f:
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

output_file = "output.csv"

# output.csv가 없으면 빈 파일로 생성한다.
if not os.path.exists(output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        pass

# output.csv에서 article number를 가져와, 그 값이 article_number_set에 있으면 set에서 제거한다.
with open(output_file, 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    for line in rdr:
        article_number = line[0] 
        if article_number in article_number_set:
            article_number_set.remove(article_number)

# ThreadPoolExecutor를 이용하여 여러 개의 스파이더를 동시에 실행한다.
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(run_spider, list(article_number_set))

print(time.time() - start) # 현재시각-시작시간 = 실행시간
