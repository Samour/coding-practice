# Connecting to PostgreSQL server

Connection URL: `sql-learn-pg.csy1idkfvupb.ap-southeast-2.rds.amazonaws.com:5432`

TLS1.2 is enforced

If you are using a secrets file, you can load your username/password by running

```
source .secrets
```

Connection command:

```
psql -h sql-learn-pg.csy1idkfvupb.ap-southeast-2.rds.amazonaws.com -p 5432 "dbname=playdb user=$DB_USERNAME password=$DB_PASSWORD sslrootcert=global-bundle.pem"
```
