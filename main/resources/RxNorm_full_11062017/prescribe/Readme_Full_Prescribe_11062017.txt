November 06, 2017

README: RxNorm 11/06/2017 Current Prescribable Content
=====================================================

-----------------------------------------------------------------
This Current Prescribable Content release contains data that is 
consistent with the 2017AB version of the UMLS.   
-----------------------------------------------------------------

This release has been created from the November 06, 2017 Full 
Release version of RxNorm. 

For full details, please refer to the RxNorm documentation at 
http://www.nlm.nih.gov/research/umls/rxnorm/docs/prescribe.html.  

This release contains database control files and SQL
commands for use in the automation of the loading process of
these files into an Oracle or MySQL database.  
 
RxNorm release data files are available by download from
the NLM download server at:

        http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html

This link will allow you to download the latest files (no login required):
RxNorm_full_prescribe_11062017.zip

Once downloaded, it must be unzipped in order to access the files.

HARDWARE AND SOFTWARE RECOMMENDATIONS
-------------------------------------
- Supported operating systems:
	Windows: 7
	Linux
	Solaris: Solaris 10 

- Hardware Requirements

  - A MINIMUM 502 MB of free hard disk space (To accomodate ZIP files and 
	unzipped contents).  


CONTENTS OF THE ZIP FILE
-------------------------

The ZIP formatted file is 65,604,212 bytes and contains the 
following 16 files and 4 directories:

	Readme_Full_Prescribe_11062017.txt	2,617	bytes

rrf directory:

	RXNCONSO.RRF		 29,382,427	bytes
	RXNREL.RRF		185,348,489	bytes		
	RXNSAT.RRF		243,734,953	bytes 

scripts directory:

	oracle sub-directory:

	RXNCONSO.ctl			512		bytes
	RXNREL.ctl			471		bytes
	RXNSAT.ctl			378		bytes
	RxNormDDL.sql			1,373		bytes
	rxn_index.sql			460		bytes
	populate_oracle_rxn_db.bat	699		bytes

	mysql sub-directory:

	Indexes_mysql_rxn.sql		463		bytes	
	Load_scripts_mysql_rxn_unix.sql	1,469		bytes
	Load_scripts_mysql_rxn_win.sql	1,468		bytes
	Populate_mysql_rxn.bat		777		bytes
	populate_mysql_rxn.sh		1,609		bytes
	Table_scripts_mysql_rxn.sql	1,749		bytes

	
Additional NOTES:
-----------------

- Most RxNorm users will need applications and data management
  systems such as an RDBMS for storage and retrieval.

- The RxNorm release files contain UTF-8 Unicode encoded data.

- Refer to the RxNorm prescribing release documentation at http://www.nlm.nih.gov/research/umls/rxnorm/docs/prescribe.html 
  for information on the contents of the RxNorm Current Prescribable Content Release Files.
