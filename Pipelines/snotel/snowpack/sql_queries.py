basin_table_create = (""" CREATE TABLE IF NOT EXISTS basins(
                            basin_id serial PRIMARY KEY ,
                            basin_name CHAR(20) NOT NULL)
                        """)

location_table_create = ("""CREATE TABLE IF NOT EXISTS locations (
                            location_id SERIAL PRIMARY KEY,
                            location_name CHAR(50) NOT NULL,
                            elevation INT,
                            region_id INT REFERENCES basins(basin_id) 
                            );""")

snowpack_table_create = ("""CREATE TABLE IF NOT EXISTS snowpack (
                            id SERIAL PRIMARY KEY,
                            location_id INT NOT NULL,
                            date DATE NOT NULL 
                            );""")
basin_aggregate_table_create = (
                    """
                    CREATE TABLE IF NOT EXISTS basins_aggregate (
                            region INT NOT NULL,
                            pct_median INT,
                            pct_avg INT, 
                            date DATE NOT NULL);""")


basinID_select = ("""SELECT  basin_id 
                  FROM basins
                  WHERE basins.basin_name = %s;""")

basins_table_insert = ("""INSERT INTO basins (basin_name) VALUES (%s) RETURNING basin_id;""")
location_table_insert = ("""INSERT INTO locations (location_name, elevation, region_id) VALUES (%s, %s, %s);""")
