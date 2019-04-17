#create a module for MAO classes like "avoid_the_consumption_of_XXX"
#then merge to MedAct.owl

DOWNLOAD=curl -o
REF_ONTOLOGY_DIR=../other_ontology/

../MedAct.owl:avoid_foods-merged.owl
	robot merge --input $@ --input $< --output $@
	rm $<

avoid_foods-merged.owl:avoid_foods.owl xfoodon.owl xro.owl
	robot merge --input avoid_foods.owl --input xfoodon.owl --input xro.owl --output $@
	rm $^

avoid_foods.owl:avoid_foods.tsv ${REF_ONTOLOGY_DIR}foodon-merged.owl
	dosdp-tools generate --obo-prefixes=true --prefixes=../pattern/prefixes.yaml --template=../pattern/avoid_consumption_of_foods.yaml --infile=avoid_foods.tsv --ontology=../other_ontology/foodon-merged.owl --outfile=$@

${REF_ONTOLOGY_DIR}foodon-merged.owl:${REF_ONTOLOGY_DIR}foodon.owl
	robot merge --input $< --output $@

${REF_ONTOLOGY_DIR}foodon.owl:
	mkdir -p ../other_ontology
	$(DOWNLOAD) $@ 'https://raw.githubusercontent.com/FoodOntology/foodon/master/foodon.owl'

xfoodon.owl:${REF_ONTOLOGY_DIR}foodon-merged.owl food_terms.tsv
	robot extract --method BOT --input ../other_ontology/foodon-merged.owl --term-file food_terms.tsv --output xfoodon.owl -p "FOODON:http://purl.obolibrary.org/obo/FOODON_"
	rm food_terms.tsv

food_terms.tsv:avoid_foods.tsv
	cut -f 2 $< | sed '1d' > $@

xro.owl:${REF_ONTOLOGY_DIR}ro.owl ro_terms.tsv
	robot extract --method BOT --input ../other_ontology/ro.owl --term-file ro_terms.tsv --output xro.owl

${REF_ONTOLOGY_DIR}ro.owl:
	mkdir -p ../other_ontology/
	$(DOWNLOAD) $@ 'https://raw.githubusercontent.com/oborel/obo-relations/master/ro.owl'

