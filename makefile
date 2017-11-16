DOWNLOAD=curl -o

#find references in UMLS by run the Java program


#find the most terms (short sentences <= 10 words) with ExtractMostFrequentSens.py
#the same script also finds the original Gene Reviews file that the terms come from

#seperate the text file into different sections with seperateManigementSections.py

#parse XML file to extract all test
main/resources/Gene_Reviews_Extracted:main/resources/gene_NBK1116
	python main/scripts/XML_parser.py

#unzip and then delete original file
main/resources/gene_NBK1116:main/resources/gene_NBK1116.tar.gz
	tar -xzvf $<
	#rm $<
#Download Gene Reviews
main/resources/gene_NBK1116.tar.gz:
	$(DOWNLOAD) $@ 'ftp://ftp.ncbi.nlm.nih.gov/pub/litarch//ca/84/gene_NBK1116.tar.gz'
