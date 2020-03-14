from Pipelines.snotel.snowpack.backfill_snopack import extract_snowpack_data
from Pipelines.snotel.snowpack.create_tables_queries import basin_table_create, basin_aggregate_table_create,\
    snowpack_table_create, location_table_create
import psycopg2
regions_dict = extract_snowpack_data()
regions = list(regions_dict.keys())[3:]
locations = []
for region in regions:
    locs = list(regions_dict[region].keys())
    for l in locs:
        locations.append(l)
#
# regions = ['SPOKANE', 'UPPERCOLUMBIA', 'CENTRALCOLUMBIA', 'UPPERYAKIMA', 'LOWERYAKIMA', 'WALLAWALLA',
#            'LOWERSNAKE', 'LOWERCOLUMBIA', 'SOUTHPUGETSOUND', 'CENTRALPUGETSOUND', 'NORTHPUGETSOUND', 'OLYMPIC']

create_table_queries = [ basin_table_create, snowpack_table_create, basin_aggregate_table_create, location_table_create]

def execute_create_table_queries(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

# def insert_basins(regions, cur):
#     for region in regions:
#         cur.execute(basins_table_insert, (region,))


def main():
    """

    This main function creates a new database session and a new cursor to process
    song data and log data by calling function <process_data>
    """

    conn = psycopg2.connect("host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com dbname=kaladindb user=postgres password=tchoob89")
    cur = conn.cursor()
    cur.execute(location_table_create)

    execute_create_table_queries(cur, conn)

    conn.close()
    # create_tables(cur, conn)
    #
    # regions_dict = extract_snowpack_data()
    #
    # regions = list(regions_dict.keys())[3:]
    # locations = []
    # for region in regions:
    #     locs = list(regions_dict[region].keys())
    #     # cur.execute(basins_table_insert, (region,))
    #     # conn.commit()
    #
    #     for l in locs:
    #         locations.append(l)
    #
    # cur.execute(basin_table_create)
    # conn.commit()
    #
    #
    #
    # conn.close()


if __name__ == "__main__":
    main()