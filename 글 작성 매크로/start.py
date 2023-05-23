from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen

such = input("검색어: ")

id = 'user'
pw = 'user'

# 크롬 옵션
chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_argument('--headless')

# 브라우저 실행
driver = webdriver.Chrome("./chromedriver", options=chromeOptions)
driver.get('http://172.16.24.199:8000/login')
# 브라우저 사이즈 변경
totalHight = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(1280,totalHight)

driver.find_element(By.NAME, '')

body = driver.find_element(By.XPATH, '/html/body')
for x in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    print('%d회 스크롤'%(x))

imgs = driver.find_elements(By.CSS_SELECTOR,'img._image')


driver.quit()
