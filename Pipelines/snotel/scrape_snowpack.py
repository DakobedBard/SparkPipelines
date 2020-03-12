from bs4 import BeautifulSoup
import requests
import datetime
from Pipelines.data_utils.mongoConnection import getMongoClient

def extract_snowpack_data():
    url = 'https://wcc.sc.egov.usda.gov/reports/UpdateReport.html?report=Washington'
    r = requests.get(url)
    html = r.content

    soup = BeautifulSoup(html, 'html.parser')
    snowpackTable = soup.find('table', {'id': 'update_report_data'})

    metrics = ['Elev (ft) ', 'Snow Current (in)', 'Snow Median (in)', 'Snow Pct of Median', 'Water Current ',
               'Water Average (in)', 'Water Pct of Average']

    region_dictionary = {}
    currentdate = datetime.datetime.now()
    todayyear = currentdate.year
    todaymonth = currentdate.month
    todayday = currentdate.day

    region_dictionary['year'] = todayyear
    region_dictionary['month'] = todaymonth
    region_dictionary['day'] = todayday

    for i, row in enumerate(snowpackTable.select('tr')):
        columns = row.find_all('td')
        if len(columns) == 1:
            # Okay this is or region...  i.e SPOKANE, LOWERCOLUMBIA etc... As this row will always precede the associated data rows and basin index rows, here we set the current_region variable which will be used by the subsequent conditional statements..
            col_text = columns[0].getText()
            region_name = ''.join(filter(str.isalpha, col_text))

            current_region = region_name

            region_dictionary[region_name] = {}

        if len(columns) == 3:

            # Here we have our basin index.. which has aggregate values such as percentage of median etc for the basin
            for j, column in enumerate(columns):
                column_text = column.getText()
                if j == 1:

                    pct_med = int(''.join(filter(str.isdigit, column_text)))
                    region_dictionary[current_region]['Basin Index'] = {}
                    region_dictionary[current_region]['Basin Index']['pctmedian'] = pct_med
                elif j == 2:
                    pct_avg = int(''.join(filter(str.isdigit, column_text)))
                    region_dictionary[current_region]['Basin Index']['pctavg'] = pct_avg

        if len(columns) == 8:
            ## This is the actual data...  We have 8 data columns as defined in the metrics variable.  For each region there are multiple locations at which

            for j, column in enumerate(columns):
                column_text = column.getText()
                if j == 0:
                    current_loc = column_text.split('\xa0\xa0')[1]
                    if "." in current_loc:
                        current_loc = current_loc.replace(".", "")

                    # This is to handle a corner case
                    region_dictionary[current_region][current_loc] = {}
                else:
                    try:
                        region_dictionary[current_region][current_loc][metrics[j - 1]] = int(
                            ''.join(filter(str.isdigit, column_text)))
                    except:
                        region_dictionary[current_region][current_loc][metrics[j - 1]] = ''

    return region_dictionary

def insert_snotel_to_mongodb():
    '''
    This function will instantiate a mongodb connection and insert the regions dictionary into the
    '''
    regions_dictionary = extract_snowpack_data()
    client = getMongoClient()
    snow_db = client['SnowPack']
    snow_collection = snow_db['snow_collection']
    snow_collection.insert_one(regions_dictionary)

