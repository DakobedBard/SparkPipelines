basin_table_create = (""" CREATE TABLE IF NOT EXISTS basins(
                            basin_id serial PRIMARY KEY ,
                            basin_name CHAR(20) NOT NULL)
                        """)

basins_table_insert = ("""INSERT INTO basins (basin_name) VALUES (%s);""")

location_table_create = ("""CREATE TABLE IF NOT EXISTS locations (
                            location_id SERIAL PRIMARY KEY,
                            location_name CHAR(50) NOT NULL,
                            elevation INT 
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
