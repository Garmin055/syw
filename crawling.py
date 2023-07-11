import sys
import subprocess

try:
    from selenium import webdriver
    import sqlite3

except:
    subprocess.check_call([sys.executable, '-m', 'pip3', 'install', '--upgrade', 'pip'])

    subprocess.check_call([sys.executable, '-m', 'pip3', 'install', '--upgrade', 'request.txt'])

# 데이터베이스 연결
databass = 'data/board.db'
conn = sqlite3.connect(databass)
c = conn.cursor()

# 급식 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS lunch
             (date TEXT NOT NULL,
              content TEXT NOT NULL)''')

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

driver.get('https://seoyeon.hs.kr/lunch.lunch_list')

lunchList = []

try:
    for y in range(2,8):
        for x in range(2,7):
            print(driver.find_element_by_xpath(f'/html/body/div/div/section/div/div/div[2]/div[2]/div/table/tbody/tr[{y}]/td[{x}]/div/div/div/div[2]/span/a').text)
            print('======================')
except:
    print('크롤링 완료')
    driver.get('https://seoyeon.hs.kr/')