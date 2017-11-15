::
:: Database connection parameters
:: Please edit these variables to reflect your environment
::
 set MYSQL_HOME="C:\Program Files\MySQL\MySQL Server 5.0"
 set user=
 set password=
 set host_name=
 set db_name=
 set max_error_count=0
 
 
 ATTRIB +R %logfile%   

echo ----------------------------------------
echo Starting ...
echo ----------------------------------------
echo.

 %MYSQL_HOME%\bin\mysql -u %user%  -p%password% -h%host_name% --local-infile=1 %db_name% < Table_scripts_mysql_rxn.sql  >> mysql.log 2>&1

 %MYSQL_HOME%\bin\mysql -u %user%  -p%password% -h%host_name%  --local-infile=1 %db_name% < Load_scripts_mysql_rxn_win.sql >> mysql.log 2>&1




echo
echo ----------------------------------------
echo Finished
echo ----------------------------------------
