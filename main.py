from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import urllib.request
import wget
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

'''
y = 1080
for i in range(0,5):
    location = f"window.scrollTo(0, {y})"
    driver.execute_script(location) 
    y = y + 600
    time.sleep(3)
'''

image_link = list(driver.find_elements(By.CSS_SELECTOR,"#islrg div.islrc div.isv-r.PNCib.MSM1fd.BUooTd a.wXeWr.islib.nfEiy div.bRMDJf.islir img.rg_i.Q4LuWd"))

image_src = list(map(lambda a: a.get_attribute('src'),image_link))

#print(image_src)#Sva75c.WaWKOe.RfPPs div.DyeYj div.A8mJGd.JgfpDb div.dFMRD div.pxAole div.tvh9oe.BIB1wf c-wiz.Y6heUd.qmmlRd div.nIWXKc.JgfpDb div.OUZ5W div.zjoqD div.qdnLaf.isv-id.b0vFpe div.v4dQwb a.eHAdSb img.n3VNCb.KAlRDb


# download the image
count = 1
for url in image_link:
    #count = count + 1
    url.click()
    time.sleep(3)
    link_url = driver.find_element(By.CSS_SELECTOR,".n3VNCb.KAlRDb").get_attribute('src')
    print(link_url)
    filename = "images/" + link_url.split('/')[-1]
    urllib.request.urlretrieve(link_url, filename)
    time.sleep(2)
    
