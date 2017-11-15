::
:: Database connection parameters
:: Please edit these variables to reflect your environment
::
:: set ORACLE_HOME=
:: set user=
:: set password=
:: set tns_name=

echo ----------------------------------------
echo Starting ... 
echo ----------------------------------------
echo. 

%ORACLE_HOME%\bin\sqlplus %user%/%password%@%tns_name% < RxNormDDL.sql

%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNATOMARCHIVE.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNCONSO.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNDOC.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNREL.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNSAB.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNSAT.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNSTY.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNCUICHANGES.ctl"
%ORACLE_HOME%\bin\sqlldr %user%/%password%@%tns_name% control="RXNCUI.ctl"

echo
echo ----------------------------------------
echo Finished  
echo ----------------------------------------
