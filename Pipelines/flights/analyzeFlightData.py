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

def parseRDD(airline_rdd):
    columns = split_csvstring(airline_rdd.first())

    return columns