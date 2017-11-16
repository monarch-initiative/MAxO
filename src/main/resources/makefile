ontologies=chebi.owl chebi.obo hp.obo hp.owl mesh-c mesh-d mesh-q ro.obo ro.owl RxNorm uberon.owl uberon.obo

DOWNLOAD=curl -o

all: $(ontologies)

chebi.owl:
	$(DOWNLOAD) $@ 'ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology//chebi.owl'
 
chebi.obo:
	$(DOWNLOAD) $@ 'ftp://ftp.ebi.ac.uk/pub/databases/chebi/ontology//chebi.obo'

hp.obo:
	$(DOWNLOAD) $@ 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.obo'

hp.owl:
	$(DOWNLOAD) $@ 'https://raw.githubusercontent.com/obophenotype/human-phenotype-ontology/master/hp.owl'

# This file was downloaded from https://bioportal.bioontology.org/ontologies/MESH and it is not the newest release
mesh-c:
	$(DOWNLOAD) $@ 'ftp://nlmpubs.nlm.nih.gov/online/mesh//2017/asciimesh/c2017.bin'

mesh-d:
	$(DOWNLOAD) $@ 'ftp://nlmpubs.nlm.nih.gov/online/mesh//2017/asciimesh/d2017.bin'

mesh-q:
	$(DOWNLOAD) $@ 'ftp://nlmpubs.nlm.nih.gov/online/mesh//2017/asciimesh/q2017.bin'

RxNorm:
	echo "RxNorm requires login to download"

ro.obo:
	$(DOWNLOAD) $@ 'https://raw.githubusercontent.com/oborel/obo-relations/master/ro.obo'

ro.owl:
	$(DOWNLOAD) $@ 'https://raw.githubusercontent.com/oborel/obo-relations/master/ro.owl'
 
uberon.obo:
	$(DOWNLOAD) $@ 'http://ontologies.berkeleybop.org/uberon/ext.obo'

uberon.owl:
	$(DOWNLOAD) $@ 'http://ontologies.berkeleybop.org/uberon/ext.owl'

.PHONY: clean

clean:
	rm *.owl *.obo
