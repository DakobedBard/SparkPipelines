from Pipelines.snotel.snowpack.backfill_snopack import backfill_data_urls,extract_snowpack_data

from datetime import date
from bs4 import BeautifulSoup
import requests
import datetime
startdate = date(2019, 2, 19)   # start date
enddate = date(2019, 2, 20)   # end date
urls = backfill_data_urls(startdate,enddate)

for url in urls:
    snowpack = extract_snowpack_data(url)
