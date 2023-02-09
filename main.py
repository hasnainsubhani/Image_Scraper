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
keyword = "amitabh bachan"
No_Of_Images = 50

driver.get(f"{baseurl}search?q={keyword}")
time.sleep(3)

link_lst = list(driver.find_elements(By.CSS_SELECTOR,"#pTwnEc.yg51vc div#hdtb-msb.IC1Ck div div.MUFPAc div.hdtb-mitem a"))
link_url = list(map(lambda a: a.get_attribute('href'),link_lst))
link_text = list(map(lambda a: a.get_attribute('text'),link_lst))

image_index = 0
for i in range(0,len(link_text)):
    if link_text[i] == "Images":
        image_index = i
        break

driver.get(f"{link_url[image_index]}")
time.sleep(3)


y = 1080
for i in range(0,10):
    location = f"window.scrollTo(0, {y})"
    driver.execute_script(location) 
    y = y + 900
    time.sleep(3)


image_link = list(driver.find_elements(By.CSS_SELECTOR,"#islrg div.islrc div.isv-r.PNCib.MSM1fd.BUooTd a.wXeWr.islib.nfEiy div.bRMDJf.islir img.rg_i.Q4LuWd"))

# download the image
count = 1
for url in image_link:
    #count = count + 1
    if count > No_Of_Images:
        driver.close()
        break
    try:
        url.click()
        time.sleep(3)
        link_url = driver.find_element(By.CSS_SELECTOR,".n3VNCb.KAlRDb").get_attribute('src')
        #print(link_url)
        filename = "images/" + link_url.split('/')[-1]
        urllib.request.urlretrieve(link_url, filename)
        count = count + 1
    except:
        pass
