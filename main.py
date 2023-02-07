from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import urllib.request
import time
import json


option = Options()
option.headless = False
driver = webdriver.Firefox(options=option)
driver.implicitly_wait(7)
baseurl = "https://www.google.com/"
keyword = "roses"

driver.get(f"{baseurl}search?q={keyword}")
time.sleep(3)

link_lst = list(driver.find_elements(By.CSS_SELECTOR,"#pTwnEc.yg51vc div#hdtb-msb.IC1Ck div div.MUFPAc div.hdtb-mitem a"))
link_url = list(map(lambda a: a.get_attribute('href'),link_lst))
driver.get(f"{link_url[0]}")
time.sleep(3)

y = 1080
for i in range(0,5):
    location = f"window.scrollTo(0, {y})"
    driver.execute_script(location) 
    y = y + 400
    time.sleep(3)

image_link = list(driver.find_elements(By.CSS_SELECTOR,"#islrg div.islrc div.isv-r.PNCib.MSM1fd.BUooTd a.wXeWr.islib.nfEiy"))

image_src = list(map(lambda a: a.get_attribute('src'),image_link))

# download the image
count = 1
for src in image_src:
    urllib.request.urlretrieve(src, f"images\img_{count}.png")
    count = count + 1
