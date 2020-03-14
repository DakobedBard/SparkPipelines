export RDSHOST="adolindb.cju35raiyeyw.us-west-2.rds.amazonaws.com"
export PGPASSWORD="$(aws rds generate-db-auth-token --hostname $RDSHOST --port 5432 --region us-west-2 --username postgres )"

# Connect to the amazon RDS database using the psql cli 
psql --host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com --port=5432 --username=postgres --password  --dbname=kaladindb

