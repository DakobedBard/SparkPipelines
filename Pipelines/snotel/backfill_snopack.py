url = 'https://wcc.sc.egov.usda.gov/reports/UpdateReport.html?textReport=Washington&textRptKey=12&textFormat=SNOTEL+Snow%2FPrecipitation+Update+Report&StateList=12&RegionList=Select+a+Region+or+Basin&SpecialList=Select+a+Special+Report&MonthList=April&DayList=11&YearList=2019&FormatList=N0&OutputFormatList=HTML&textMonth=March&textDay=11&CompYearList=select+a+year'''

from datetime import date, timedelta
months = ['January', 'Febuary', 'March', 'April','May','June','July','August','September', 'October', 'November', 'December']

def generate_url(month, day, year):
    return 'https://wcc.sc.egov.usda.gov/reports/UpdateReport.html?textReport=Washington&textRptKey=12&textFormat=SNOTEL+Snow%2FPrecipitation+Update+Report&StateList=12&RegionList=Select+a+Region+or+Basin&SpecialList=Select+a+Special+Report&MonthList={}&DayList={}&YearList={}&FormatList=N0&OutputFormatList=HTML&textMonth=March&textDay=11&CompYearList=select+a+year'.format(month, day, year)

def backfill_data(startdate, enddate):
    delta = enddate - startdate  # as timedelta
    urls = []
    for i in range(delta.days + 1):
        day = startdate + timedelta(days=i)
        urls.append(generate_url(months[day.month], day.day, day.year))
    return urls

    return days
startdate = date(2008, 8, 15)   # start date
enddate = date(2008, 9, 18)   # end date

urls = backfill_data(startdate, enddate)