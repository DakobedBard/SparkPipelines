from bs4 import BeautifulSoup
from selenium import webdriver
import time
def getDynamicJSContent(url, diver):
    driver.get('https://www.wta.org/go-outside/trip-reports')
    bsObj = BeautifulSoup(driver.page_source,'html.parser')
    dynamicContent = bsObj.find("div", {"class": "js-tab-target"})
    return dynamicContent

url = 'https://www.wta.org/go-outside/trip-reports'
driver = webdriver.Firefox()

content = None
while content==None:
    content = getDynamicJSContent(url, driver)
    if content==None:
        print("Inconsistent!")
        time.sleep(2)
        