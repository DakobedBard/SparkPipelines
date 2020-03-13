from Pipelines.snotel.snowpack.backfill_snopack import backfill_data_urls,extract_snowpack_data
from datetime import date
from Pipelines.data_utils.mongoConnection import getMongoClient
import requests
import datetime
startdate = date(2019, 2, 19)   # start date
enddate = date(2019, 2, 20)   # end date
urls = backfill_data_urls(startdate,enddate)
client = getMongoClient()
snow_db = client['Snow-Pack-Data']
snow_collection = snow_db['snow_collection']

for year in range(2008, 2009):
    startdate = date(year, 1, 1)  # start date
    enddate = date(year+1, 1, 1)  # end date
    urls = backfill_data_urls(startdate, enddate)
    snowpack_dictionaries = []
    for i, url in enumerate(urls):
        print("Processing " + str(i))
        snowpack_dictionaries.append(extract_snowpack_data(url))
    snow_collection.insert_many(snowpack_dictionaries)
