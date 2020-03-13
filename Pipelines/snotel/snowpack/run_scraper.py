from Pipelines.snotel.snowpack.backfill_snopack import backfill_data_urls,extract_snowpack_data

from datetime import date
from bs4 import BeautifulSoup
import requests
import datetime
startdate = date(2019, 8, 15)   # start date
enddate = date(2019, 8, 18)   # end date
urls = backfill_data_urls(startdate,enddate)

for url in urls:
    snowpack = extract_snowpack_data(url)
