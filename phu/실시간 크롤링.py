from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size=1024,768')
options.add_argument("--disable-gpu")

def crawl_data():
    def parse():
        t=1
        for i in range(3, 13):
            page_num = '//*[@id="container"]/div/div/div/div[1]/div/div/div/a[{}]'.format(i)
            next_page = driver.find_element(By.XPATH, page_num).click()
            time.sleep(1)
            #페이지 번호 넘기기
            for t in range(1,30,2):
                a_tags = driver.find_elements(By.CSS_SELECTOR, '#container > div > div > div > div.section_h12 > div > div > table:nth-child({}) > tbody > tr > td > table > tbody > tr:nth-child(1) > td > a'.format(t))
                #페이지당 15개 URL 긁기
                for a_tag in a_tags:
                    href = a_tag.get_attribute("href")
                    print(href)
                    text_url.append(href)
                    url_list['Url'] = text_url
                    # df = pd.DataFrame(url_list)
                #tag에서 URL 추출한 뒤 url_list에 저장
        if i == 12:
            time.sleep(1)
            page_num2 = '//*[@id="container"]/div/div/div/div[1]/div/div/div/a[13]'
            n_page = driver.find_element(By.XPATH, page_num2)
            n_page.click()
            i = 3
            parse()
            #10페이지 버튼인 a태그 12일때 다음페이지 버튼인 a태그 13을 클릭
    #데이터프레임 저장용
    url_list = {}
    text_url = []

    #크롬 드라이버로 웹 브라우저 실행
    path = "C:\chromedriver.exe"
    driver = webdriver.Chrome(options=options)
    time.sleep(1)

    #프라임경제 홈페이지
    driver.get("http://www.newsprime.co.kr/")
    time.sleep(1)

    #자본시장 = li[1] ~ AI 뉴스룸 = li[9]
    submenu = driver.find_element(By.XPATH,'//*[@id="header"]/div/div[3]/div/div[1]/ul/li[1]/a')
    submenu_name = submenu.text
    submenu.click()
    time.sleep(1)

    #자본시장_금융 div[1]/a[1], 자본시장_일반 div[1]/a[5], 지역_공지 div[8]/a[8]
    element = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[3]/div/div[2]/div[1]/a[6]')
    file_name_part = element.text
    element.click()
    time.sleep(1)

    # #1~10 페이지 이동 
    try:
        parse() #무한루프 함수
    except:
        df = pd.DataFrame(url_list)
        df.to_csv('{}_{}.csv'.format(submenu_name,file_name_part))
        #끝페이지 도달시 except에 따라 url 리스트에 저장된 데이터 프레임 CSV로 저장
def run_crawling_job():
    crawl_data()

print('크롤링 시작')
crawl_data()
# 10초마다 크롤링 실행
schedule.every(30).seconds.do(run_crawling_job)
while True:
    schedule.run_pending()
    time.sleep(1)

