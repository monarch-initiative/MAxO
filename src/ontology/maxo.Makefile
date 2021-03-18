## Customize Makefile settings for maxo
## 
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile

#########################################
### Generating all ROBOT templates ######
#########################################

TEMPLATESDIR=../templates

TEMPLATES=$(patsubst %.tsv, $(TEMPLATESDIR)/%.owl, $(notdir $(wildcard $(TEMPLATESDIR)/*.tsv)))

$(TEMPLATESDIR)/%.owl: $(TEMPLATESDIR)/%.tsv $(SRC)
	$(ROBOT) merge -i $(SRC) template --template $< --output $@ && \
	$(ROBOT) annotate --input $@ --ontology-iri $(ONTBASE)/components/$*.owl -o $@

templates: $(TEMPLATES)
	echo $(TEMPLATES)

tmp/remove.txt:
	echo "HP:0025454" > $@
	echo "HP:0012029" >> $@
	echo "HP:0004360" >> $@
	echo "HP:0032368" >> $@
	echo "HP:0001941" >> $@
	echo "HP:0032369" >> $@
	echo "HP:0001948" >> $@
	echo "HP:0040145" >> $@
	echo "HP:0000843" >> $@
	echo "HP:0000829" >> $@
	
imports/hp_import.owl: mirror/hp.owl imports/hp_terms_combined.txt tmp/remove.txt
	@if [ $(IMP) = true ]; then $(ROBOT) extract -i $< -T imports/hp_terms_combined.txt --force true --method BOT \
		query --update ../sparql/inject-subset-declaration.ru \
		remove --term-file tmp/remove.txt --axioms equivalent --preserve-structure false \
		annotate --ontology-iri $(ONTBASE)/$@ --version-iri $(ONTBASE)/releases/$(TODAY)/$@ --output $@.tmp.owl && mv $@.tmp.owl $@; fi
.PRECIOUS: imports/hp_import.owl

reports/maxo-edit.owl-obo-report.tsv: maxo-edit.owl
	$(ROBOT) report -i $< --fail-on none --print 5 -o $@
	

sssom.csv:
	robot query -f csv -i $(SRC) --query ../sparql/sssom.sparql $@

tmp/unmerge_def.owl: ../scripts/unmerge_ncit_def.tsv
	$(ROBOT) template --template $< \
  --ontology-iri "$(ONTBASE)/$@" \
  --output $@

tmp/merge_def.owl: ../scripts/merge_ncit_def.tsv
	$(ROBOT) template --template $< \
  --ontology-iri "$(ONTBASE)/$@" \
  --output $@
  
unmerge: tmp/unmerge_def.owl
	$(ROBOT) merge -i $(SRC) --collapse-import-closure false unmerge -i $< convert -f ofn -o unmerge.ofn && mv unmerge.ofn $(SRC)
	
merge: tmp/merge_def.owl
	$(ROBOT) merge -i $(SRC) -i $< --collapse-import-closure false convert -f ofn -o merge.ofn && mv merge.ofn $(SRC)

replace:
	make unmerge
	make merge