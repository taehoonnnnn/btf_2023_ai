import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import time
import MySQLdb
from dotenv import load_dotenv
load_dotenv()

host_env = os.getenv("host") 
user_env = os.getenv("user") 
password_env = os.getenv("password") 
database_env = os.getenv("database") 

conn = MySQLdb.connect(
    host = host_env,
    user = user_env,
    password = password_env,
    database = database_env
)

cursor = conn.cursor()
insert_query = 'INSERT INTO url_table (url) VALUES (%s)'
select_query = 'SELECT COUNT(*) FROM url_table WHERE url = %s'

def next_page(driver,i):
    page_num = '//*[@id="container"]/div/div/div/div[1]/div/div/div/a[{}]'.format(i)
    driver.find_element(By.XPATH, page_num).click()

def parse(driver):
        time.sleep(1)
            #페이지 번호 넘기기
        for t in range(1,30,2):
            a_tags = driver.find_elements(By.CSS_SELECTOR, f'#container > div > div > div > div.section_h12 > div > div > table:nth-child({t}) > tbody > tr > td > table > tbody > tr:nth-child(1) > td > a')
            #페이지당 15개 URL 긁기
            for a_tag in a_tags:
                href = a_tag.get_attribute("href")
                print(href)
                # URL 삽입
                cursor.execute(select_query, (href,))
                result = cursor.fetchone()
                if result[0] == 0:
                    try:
                        cursor.execute(insert_query, (href,))
                        conn.commit()
                        print("URL이 성공적으로 삽입되었습니다.")
                    except MySQLdb.Error as e:
                        # 에러 발생 시 에러 메시지 출력
                        print("에러 발생:", e)
                else:
                    print("이미 존재하는 URL입니다. 삽입하지 않습니다.")
        time.sleep(1)

def crawl_data():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1024,768')
    options.add_argument("--disable-gpu")
    #크롬 드라이버로 웹 브라우저 실행
    driver = webdriver.Chrome()

    #프라임경제 홈페이지
    driver.get("http://www.newsprime.co.kr/")
    time.sleep(1)
    all_list = [6,10,6,6,4,4,8,9]
    #자본시장 = li[1] ~ AI 뉴스룸 = li[9]
    for idx, i in enumerate(all_list):
        submenu = driver.find_element(By.XPATH,f'//*[@id="header"]/div/div[3]/div/div[1]/ul/li[{idx+1}]/a')
        submenu.click()
        time.sleep(1)

        #자본시장_금융 div[1]/a[1], 자본시장_일반 div[1]/a[5], 지역_공지 div[8]/a[8]
        element = driver.find_element(By.XPATH, f'/html/body/div/div[1]/div/div[3]/div/div[2]/div[{idx+1}]/a[{i}]')
        element.click()
        time.sleep(1)
        parse(driver)
        next_page(driver,4)
        parse(driver)
        next_page(driver,5)
        parse(driver)
        next_page(driver,6)
        parse(driver)
        next_page(driver,7)
        parse(driver)
    conn.commit()
    driver.quit()

def run_crawling_job():
    crawl_data()

print('크롤링 시작')
crawl_data()
# 30초마다 크롤링 실행
schedule.every(43200).seconds.do(run_crawling_job)

while True:
    schedule.run_pending()
    time.sleep(1)

