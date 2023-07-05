import subprocess

def run_spider(article_num):
    command = f'scrapy crawl article -a article_num={article_num}'
    process = subprocess.Popen(command, shell=True)
    process.wait()

number_list = [605936, 605946, 605865, 605695, 605807, 605829, 605690, 605841, 594020, 592446]
# run_spider(592446)
for i in number_list:
    run_spider(i)

