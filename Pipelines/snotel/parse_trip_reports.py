from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

def  scrape_wta(url):
    wtaClient = uReq(url)
    wta_html = wtaClient.read()
    wtaClient.close()
    wtasoup = soup(wta_html,"html.parser")
    return wtasoup

def parse_wta_trip_reports(url):
    wtaClient = uReq(url)
    wta_html = wtaClient.read()
    wtaClient.close()
    wtasoup = soup(wta_html,"html.parser")
    return wtasoup
wta_url = 'https://www.wta.org/go-outside/trip-reports'
trip_reports = parse_wta_trip_reports(wta_url)

portal_column_content = trip_reports.select('div#portal-column-content')[0]

trips=  'https://www.wta.org/@@search_tripreport_listing?b_size=100&b_start:int=0&_=1584032147527'
trips2 = 'https://www.wta.org/@@search_tripreport_listing?b_size=100&b_start:int=300&_=1584032147526'
wtasoup = scrape_wta(trips2)

import datetime

def parse_trip_report(url):
    region = None
    trip_text = ''
    location = None
    tripClient = uReq(url)
    trip_html = tripClient.read()
    tripClient.close()
    tripsoup = soup(trip_html,"html.parser")
    content = tripsoup.find("article", {"id": "content"})

    trip_text = content.find('p').text
    region = content.find_all('span')[1].text
    trip_title = content.find('h1').text
    date = content.find('span', {"class": "elapsed-time"})
    date_string = str(date).split('datetime=')[1].split('"')[1]

    return (trip_title, region, date_string, trip_text)

first_report = 'https://www.wta.org/go-hiking/trip-reports/trip_report-2020-03-12-6028488389'
reports =  wtasoup.find_all("a", {"class": "listitem-title"})

trip_soup = parse_trip_report(first_report)
content = trip_soup.find("article", { "id" : "content" })

trip_text =  content.find('p').text
region = content.find_all('span')[1].text
trip_title = content.find('h1').text
date = content.find('span', {"class": "elapsed-time"})
date_string = str(date).split('datetime=')[1].split('"')[1]


parsed_date = datetime.datetime.strptime(date_string, '%b %d, %Y')