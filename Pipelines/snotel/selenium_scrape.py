from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

def getDynamicJSContent(url, diver):
    driver.get('https://www.wta.org/go-outside/trip-reports')
    bsObj = BeautifulSoup(driver.page_source,'html.parser')
    dynamicContent = bsObj.find("div", {"class": "js-tab-target"})
    return dynamicContent

def get_page_soup(page_url):
    client = uReq(page_url)
    page_html = client.read()
    client.close()
    page_soup = soup(page_html,"html.parser")
    return page_soup

url = 'https://www.wta.org/go-outside/trip-reports'
driver = webdriver.Firefox()

content = None
while content==None:
    content = getDynamicJSContent(url, driver)
    if content==None:
        print("Inconsistent!")
        time.sleep(2)


pagination = content.find("nav", {"class": "pagination"})
pages = content.find("nav", {"class": "pagination"})
links = pages.find_all('a')
npages  = int(links[-2].text)
pages = []
for page_number in range(3):
    url = 'https://www.wta.org/@@search_tripreport_listing?b_size=100&amp;b_start:int=%d&amp;_=1584045459199"' % int(100*page_number)
    page_soup = get_page_soup(url)
    pages.append(page_soup)