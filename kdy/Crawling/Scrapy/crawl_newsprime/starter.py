import subprocess

def run_spider(article_num):
    command = f'scrapy crawl num -a article_num={article_num}'
    process = subprocess.Popen(command, shell=True)
    process.wait()

run_spider(605936)
