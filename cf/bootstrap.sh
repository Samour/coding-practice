#!/bin/bash

. .secrets

DB_HOST="sql-learn-pg.csy1idkfvupb.ap-southeast-2.rds.amazonaws.com"
DB_PORT=5432
DB_CERT="../global-bundle.pem"
DB_CONN_ATTR="dbname=postgres user=$DB_ROOT_USERNAME password=$DB_ROOT_PASSWORD sslrootcert=$DB_CERT"

AARON_ROLE='\$AARON_ROLE\$'
AARON_PASSWORD='\$AARON_PASSWORD\$'
DEB_ROLE='\$DEB_ROLE\$'
DEB_PASSWORD='\$DEB_PASSWORD\$'

SED_SCRIPT="s/$AARON_ROLE/$DB_AARON_USERNAME/g;
s/$AARON_PASSWORD/$DB_AARON_PASSWORD/g;
s/$DEB_ROLE/$DB_DEB_USERNAME/g;
s/$DEB_PASSWORD/$DB_DEB_PASSWORD/g;"

sed "$SED_SCRIPT" bootstrap.sql \
  | psql -h $DB_HOST -p $DB_PORT "$DB_CONN_ATTR"
