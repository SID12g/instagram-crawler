from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import urllib.request
import time
import os
from dotenv import load_dotenv

load_dotenv()

# chromedriver default options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://instagram.com')

time.sleep(2)

# login instagram
e = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
e.send_keys(os.getenv('INSTAGRAM_ID'))
e = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
e.send_keys(os.getenv('INSTAGRAM_PASSWORD'))
e.send_keys(Keys.ENTER)

# move to tag = '사과'
time.sleep(4)
driver.get('https://www.instagram.com/explore/tags/%EC%82%AC%EA%B3%BC/')

# driver.get('https://www.instagram.com/p/C2ujnmyvL3v/') # for video skip test

driver.implicitly_wait(10) # max wait = 10sec (better than time.sleep)
e = driver.find_elements(By.CSS_SELECTOR, '._aagw')[0].click()

def getImage(i): 
    driver.implicitly_wait(10)
    try:
        image = driver.find_element(By.CSS_SELECTOR, '._aa1_ ._aa20 ._aagv .xu96u03').get_attribute('src')
        print(i, image)
        urllib.request.urlretrieve(image, f'{i}.jpg')
        e = driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-')
        driver.execute_script('arguments[0].click();', e)
        time.sleep(1)
    except:
        print('not img!!')
        e = driver.find_element(By.CSS_SELECTOR, '._aaqg ._abl-')
        driver.execute_script('arguments[0].click();', e)
        time.sleep(1)

for i in range(10):
    getImage(i)
        
# driver.implicitly_wait(10)
# try:
#     image = driver.find_element(By.CSS_SELECTOR, '._aa1_ ._aa20 ._aagv .xu96u03').get_attribute('src')
#     print(image, type(image))
#     urllib.request.urlretrieve(image, 'test.jpg')
#     print('end store image process')

# except: print('fail')
    
# print('end all process')
