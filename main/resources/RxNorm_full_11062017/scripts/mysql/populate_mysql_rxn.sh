# TO load the data  in shell.


#!/bin/sh -f
#
# For useful information on loading your RxNorm subset
# into a MySQL database, please consult the on-line
# documentation at:
#
# http://www.nlm.nih.gov/research/umls/rxnorm/docs/index.html
#

#
# Database connection parameters
# Please edit these variables to reflect your environment
#
MYSQL_HOME=/usr 
user=
password=
db_name=
dbserver=


/bin/rm -f mysql.log
touch mysql.log
ef=0
echo "See mysql.log for output"

echo "----------------------------------------" >> mysql.log 2>&1
echo "Starting ... `/bin/date`" >> mysql.log 2>&1
echo "----------------------------------------" >> mysql.log 2>&1
echo "MYSQL_HOME= $MYSQL_HOME" >> mysql.log 2>&1
echo "user =       $user" >> mysql.log 2>&1
echo "db_name =    $db_name" >> mysql.log 2>&1


echo "    Create and load tables ... `/bin/date`" >> mysql.log 2>&1
$MYSQL_HOME/bin/mysql -vvv -u $user -p$password -h$dbserver $db_name < Table_scripts_mysql_rxn.sql >> mysql.log 2>&1
if [ $? -ne 0 ]; then ef=1; fi

if [ $ef -ne 1 ]
then
echo "    Load Data ... `/bin/date`" >> mysql.log 2>&1
$MYSQL_HOME/bin/mysql -vvv -u $user -p$password -h$dbserver $db_name < Load_scripts_mysql_rxn_unix.sql >> mysql.log 2>&1
if [ $? -ne 0 ]; then ef=1; fi
fi


echo "----------------------------------------" >> mysql.log 2>&1
if [ $ef -eq 1 ]
then
echo "There were one or more errors.  Please reference the mysql.log file for details." >> mysql.log 2>&1
else
echo "Completed without errors." >> mysql.log 2>&1
fi
echo "Finished ... `/bin/date`" >> mysql.log 2>&1
echo "----------------------------------------" >> mysql.log 2>&1
