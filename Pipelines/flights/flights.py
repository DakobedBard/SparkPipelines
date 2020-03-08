

from Pipelines.flights.analyzeFlightData import split_csvstring, parseRDD
from Pipelines.getSparkSession import getSparkSession

import csv              # for the split_csvstring function from Part 3.2.2
try:                    # Python 3 compatibility
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def split_csvstring(input_string):
    """Parse a csv-like line and break the values into a list.
    Parameters
    ----------
    input_string (str): a csv-like string to work on
    Returns
    -------
    list : the list of the values
    Example
    -------
    >>> split_csvstring(u'a,b,0.7,"Oct 7, 2016",42,')
    ['a', 'b', '0.7', 'Oct 7, 2016', '42', '']
    """
    # we create a StringIO handler
    fio = StringIO(input_string)
    # and feed that into the csv.reader library which is (probably) the best way to parse those strings
    reader = csv.reader(fio, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)

    # obtains the first line of the reader (which should be the only line)
    row_values = next(reader)

    return row_values
def make_row_dict(row_values, col_names, keep_keys_set):
    """Extract specific columns from a row (string) and operates some specific transformations on the values.

    Parameters
    ----------
    row_values (list): a list of the values of a given row
    col_names (list): a list of all the columns in row_string ordered as in row_string
    keep_keys_dict (set): the set of the columns we keep (anything else is discarded)

    Returns
    -------
    dict : a dictionary containing the key,value pairs we chose to keep

    Example
    -------
    >>> make_row_dict(['2012', '4', 'AA', '12478', '12892', '-4.00', '0.00', '-21.00', '0.00', '0.00', ''],\
    ['YEAR', 'MONTH', 'UNIQUE_CARRIER', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID', 'DEP_DELAY', 'DEP_DELAY_NEW', 'ARR_DELAY', 'ARR_DELAY_NEW', 'CANCELLED', ''],\
    {'DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID', 'DEP_DELAY', 'ARR_DELAY'}
    {'ARR_DELAY': -17.0, 'DEST_AIRPORT_ID': '12892', 'DEP_DELAY': -4.0, 'ORIGIN_AIRPORT_ID': '12478'}
    """
    row = row_values[0].split(",")
    print(row)
    output_dict = {}
    indices = []
    for key in keep_keys_set:
        if (key in col_names):
            index = col_names.index(key)
            print(index)
            output_dict[key] = float(row[index])

    return output_dict

spark = getSparkSession()
sc = spark.sparkContext
flightsRDD = sc.textFile('data/airline-data-extract.csv')

header = flightsRDD.first()
columns = split_csvstring(header)
flightsRDD = rdd = flightsRDD.filter(lambda line: line!= header)
keys =     {'DEST_AIRPORT_ID', 'ORIGIN_AIRPORT_ID', 'DEP_DELAY', 'ARR_DELAY'}


firstTry = make_row_dict(flightsRDD.take(1),columns, keys )
