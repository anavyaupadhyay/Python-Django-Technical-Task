
# Backing up postgre to aws

To backup PostgreSQL database to Amazon S3 using s3cmd and cron.

*Install and configure s3cmd*

for Ubuntu OS
```
apt-get install s3cmd
```

Set Amazon access & secret keys using --configure option. Enable encryption for data transferring as well as HTTPS.
```
s3cmd --configure
```

*Backup the database*
```
PGPASSWORD=test pg_dump -Fc --no-acl -h localhost -U test1 test1 > backup.dump
```

*Push to Amazon S3*
```
Create a bucket
>>>s3cmd mb s3://sudofire
Push created backup to that bucket
>>>s3cmd put backup.dump s3://sudofire --encrypt
```

*Automate*

```
#!/usr/bin/env bash

APP=$1

DB_NAME=$test1
DB_USER=$test1
DB_PASS=$test

BUCKET_NAME=sudofire

TIMESTAMP=$(date +%F_%T | tr ':' '-')
TEMP_FILE=$(mktemp tmp.XXXXXXXXXX)
S3_FILE="s3://$BUCKET_NAME/$APP/$APP-backup-$TIMESTAMP"

PGPASSWORD=$DB_PASS pg_dump -Fc --no-acl -h localhost -U $DB_USER $DB_NAME > $TEMP_FILE
s3cmd put $TEMP_FILE $S3_FILE --encrypt
rm "$TEMP_FILE"
```
Save the file to backup.sh and make it executable with chmod +x. Test if it works with properly set positional parameters, e.g.
```
>>>./backup.sh acme test1 test1 test
```

Add a cron entry using crontab -e and set it to run daily at 2am

```
>>>* 02 * * * /path/to/backup.sh acme test1 test1 test
```
