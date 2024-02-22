from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyperclip
import os
from dotenv import load_dotenv

load_dotenv()
# chromedriver default options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('user-data-dir=/Users/sid12g/Library/Application Support/Google/Chrome/')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=https%3A%2F%2Fm.naver.com%2Fna%2F')

time.sleep(2)
pyperclip.copy(os.getenv('NAVER_ID')) # command+c
e = driver.find_element(By.CSS_SELECTOR, 'input[id="id"]')
e.send_keys(Keys.COMMAND, 'v')

time.sleep(1)
pyperclip.copy(os.getenv('NAVER_PASSWORD')) # command+c
e = driver.find_element(By.CSS_SELECTOR, 'input[id="pw"]')
e.send_keys(Keys.COMMAND, 'v')

time.sleep(1)
e.send_keys(Keys.ENTER)

time.sleep(2)
driver.get('https://m.blog.naver.com/FeedList.naver')

time.sleep(1.5)
driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FGoWriteForm.naver')

time.sleep(2)
e = driver.find_element(By.CSS_SELECTOR, '.documentTitle_blog .se_textarea')
e.send_keys('테스트 제목입니다.')

time.sleep(2)
e = driver.find_element(By.CSS_SELECTOR, '.se_sectionArea .se_editable')
e.send_keys('테스트 내용입니다.\n우리집 고양이 너무 귀여워요')