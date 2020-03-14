from Pipelines.snotel.snowpack.backfill_snopack import extract_snowpack_data
from Pipelines.snotel.snowpack.sql_queries import basin_table_create, basin_aggregate_table_create,\
    snowpack_table_create, location_table_create
import psycopg2
conn = psycopg2.connect("host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com dbname=kaladindb user=postgres password=tchoob89")
cur = conn.cursor()
create_table_queries = [ basin_table_create, snowpack_table_create, basin_aggregate_table_create, location_table_create]

def execute_create_table_queries(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
    conn.commit()
execute_create_table_queries(cur,conn)




conn = psycopg2.connect("host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com dbname=kaladindb user=postgres password=tchoob89")
cur = conn.cursor()
cur.execute(location_table_create)
execute_create_table_queries(cur, conn)



conn.commit()
conn.close()
from Pipelines.snotel.snowpack.backfill_snopack import extract_snowpack_data
import psycopg2
from Pipelines.snotel.snowpack.sql_queries import basins_table_insert,location_table_insert, basinID_select

conn = psycopg2.connect("host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com dbname=kaladindb user=postgres password=tchoob89")
cur = conn.cursor()
regions_dict = extract_snowpack_data()
regions_dict.pop('year')
regions_dict.pop('day')
regions_dict.pop('month')

# We will start

for region in regions_dict.keys():

    regions_dict[region].pop('Basin Index')
    locations = regions_dict[region].keys()
    cur.execute(basins_table_insert, (region,))
    basin_id  = cur.fetchone()[0]
    conn.commit()
    for location in locations:
        location_dict = regions_dict[region][location]

        elevation = location_dict['Elev (ft) ']
        cur.execute(location_table_insert, (location,elevation,basin_id))        ## This seems like a huge hack..

    conn.commit()