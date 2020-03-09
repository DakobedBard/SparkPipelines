I am practicing some data engineering concepts here 

flighs pipleline will be what I work on first.  

I was able to check for the existance of someting in the dataframes array field.  This was done using

from pyspark.sql import functions as F
containsRestaurants = FiveStarsPheonixCC.filter(array_contains(F.col("categories"), "Food"))

For some reason the col method does not want to get imported nicely in PyCharm. 