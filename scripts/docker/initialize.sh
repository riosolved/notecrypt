#!/bin/sh

# === PYTHON ===
. /scripts/python/setup.sh --file /api/requirements.txt

python /api/application.py

# === MariaDB ===
# mysqld --user=mysql --datadir=/var/lib/mysql
# mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
# /usr/bin/mariadbd-safe --datadir='/var/lib/mysql'
# mysqld --user=mysql --datadir=/var/lib/mysql