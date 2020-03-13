from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests
import datetime


def generate_url(month, day, year):
    '''
    Generate a URL that points to the snowpack data to be scraped on the input month, day and year
    :param month:
    :param day:
    :param year:
    :return: url string
    '''
    return 'https://wcc.sc.egov.usda.gov/reports/UpdateReport.html?textReport=Washington&textRptKey=12&textFormat=SNOTEL+Snow%2FPrecipitation+Update+Report&StateList=12&RegionList=Select+a+Region+or+Basin&SpecialList=Select+a+Special+Report&MonthList={}&DayList={}&YearList={}&FormatList=N0&OutputFormatList=HTML&textMonth=March&textDay=11&CompYearList=select+a+year'.format(month, day, year)

def backfill_data_urls(startdate, enddate):
    '''
    Returns a list of urls that will be scraped
    :param startdate:
    :param enddate:
    :return:
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    delta = enddate - startdate  # as timedelta
    urls = []
    for i in range(delta.days + 1):
        day = startdate + timedelta(days=i)
        urls.append(generate_url(months[day.month-1], day.day, day.year))
    return urls

def extract_snowpack_data(url):
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

                    try:
                        pct_med = int(''.join(filter(str.isdigit, column_text)))
                    except:
                        pct_med = 0
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

