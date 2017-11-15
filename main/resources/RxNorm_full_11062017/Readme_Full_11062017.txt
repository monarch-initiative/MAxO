November 06, 2017

README: RxNorm 11/06/2017 Full Update Release
===================================================

-----------------------------------------------------------------
This Full release contains data that is consistent with the 
2017AB version of the UMLS.   
-----------------------------------------------------------------

This release contains updates to the following nine sources: 

ATC - ATC_2017 (Anatomical Therapeutic Chemical Classification System )
GS - 09/28/2017 (Gold Standard Alchemy)
CVX - 08/25/2017 (Vaccines Administered, 2017_06_30)
MMSL - 10/01/2017 (Multum MediSource Lexicon) 
MMX - 09/25/2017 (Micromedex DRUGDEX)  
MTHSPL - 10/27/2017 (FDA Structured Product Labels) 
NDDF - 09/27/2017 (First Databank FDB MedKnowledge (formerly NDDF Plus))
NDFRT - 11/06/2017 (National Drug File - Reference Terminology)
VANDF - 08/24/2017 (Veterans Health Administration National Drug File)
DRUGBANK - 09/27/2017 (DrugBank, 5.0_2017_08_01)

For full details, please refer to the RxNorm documentation at 
http://www.nlm.nih.gov/research/umls/rxnorm/docs/index.html.  

This release contains database control files and SQL
commands for use in the automation of the loading process of
these files into an Oracle RDBMS.  In addition, scripts are now 
provided for loading the RxNorm files into a MySQL database.
 
RxNorm release data files are available by download from
the NLM download server at:

        http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html

This link will take you to a page for downloading the latest files:
RxNorm_full_11062017.zip

Once downloaded, it must be unzipped in order to access the files.

HARDWARE AND SOFTWARE RECOMMENDATIONS
-------------------------------------
- Supported operating systems:
	Windows: 7
	Linux
	Solaris: Solaris 10

- Hardware Requirements

  - A MINIMUM 1.84 GB of free hard disk space (To accomodate ZIP files and 
	unzipped contents).  


CONTENTS OF THE ZIP FILE
-------------------------

The ZIP formatted file is 239,852,821 bytes and contains the 
following 44 files and 9 directories:

	Readme_Full_11062017.txt	4,135	bytes

rrf directory:

	RXNCONSO.RRF		123,520,562		bytes
	RXNDOC.RRF	        207,278	        	bytes
	RXNREL.RRF		468,266,304     	bytes
	RXNSAB.RRF		12,154		        bytes		
	RXNSAT.RRF		567,589,006		bytes 
	RXNSTY.RRF		17,918,230		bytes
	RXNATOMARCHIVE.RRF	38,159,465		bytes
	RXNCUICHANGES.RRF	538,640	         	bytes
	RXNCUI.RRF		1,406,138      		bytes

scripts directory:

	oracle sub-directory:

	RXNATOMARCHIVE.ctl		564		bytes
	RXNCONSO.ctl			512		bytes
	RXNCUI.ctl			296		bytes
	RXNCUICHANGES.ctl		346		bytes
	RXNDOC.ctl			248		bytes
	RXNREL.ctl			471		bytes
	RXNSAB.ctl			674		bytes	
	RXNSAT.ctl			378		bytes
	RXNSTY.ctl			267		bytes
	RxNormDDL.sql			3,291		bytes
	rxn_index.sql			660		bytes
	populate_oracle_rxn_db.bat	1,164		bytes

	mysql sub-directory:

	Indexes_mysql_rxn.sql		662		bytes	
	Load_scripts_mysql_rxn_unix.sql	3,961		bytes
	Load_scripts_mysql_rxn_win.sql	3,959		bytes
	Populate_mysql_rxn.bat		775		bytes
	populate_mysql_rxn.sh		1,609		bytes
	Table_scripts_mysql_rxn.sql	4,205		bytes


prescribe directory

	Readme_Full_Prescribe_11062017.txt	2,617	bytes
	
	rrf subdirectory:
	
	RXNCONSO.RRF		 29,382,427	bytes
	RXNREL.RRF		185,348,489	bytes
	RXNSAT.RRF		243,734,953	bytes

	scripts sub-directory:

		oracle sub-directory:

		RXNCONSO.ctl			512	bytes
		RXNREL.ctl			471	bytes
		RXNSAT.ctl			378	bytes
		RxNormDDL.sql			1,373	bytes
		rxn_index.sql			460	bytes
		populate_oracle_rxn_db.bat	699	bytes

		mysql sub-directory:

		Indexes_mysql_rxn.sql		463	bytes	
		Load_scripts_mysql_rxn_unix.sql	1,469	bytes
		Load_scripts_mysql_rxn_win.sql	1,468	bytes
		Populate_mysql_rxn.bat		777	bytes
		populate_mysql_rxn.sh		1,609	bytes
		Table_scripts_mysql_rxn.sql	1,749	bytes

	
Additional NOTES:
-----------------

- Most RxNorm users will need applications and data management
  systems such as an RDBMS for storage and retrieval.

- The RxNorm release files contain UTF-8 Unicode encoded data.

- Refer to the RxNorm release documentation at http://www.nlm.nih.gov/research/umls/rxnorm/docs/index.html
