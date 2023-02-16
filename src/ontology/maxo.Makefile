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

imports/pr_import.owl: mirror/pr.owl imports/pr_terms_combined.txt
	if [ $(IMP) = true ]; then $(ROBOT) extract -i $< -T imports/pr_terms_combined.txt --force true --method BOT \
		annotate --ontology-iri $(ONTBASE)/$@ $(ANNOTATE_ONTOLOGY_VERSION) --output $@.tmp.owl && mv $@.tmp.owl $@; fi
.PRECIOUS: imports/pr_import.owl

$(IMPORTDIR)/hp_import.owl: $(MIRRORDIR)/hp.owl $(IMPORTDIR)/hp_terms_combined.txt
	if [ $(IMP) = true ]; then $(ROBOT) extract  -i $< -T $(IMPORTDIR)/hp_terms_combined.txt --copy-ontology-annotations true --force true --method BOT \
		remove --base-iri $(URIBASE)/HP --axioms external --preserve-structure false --trim false \
		query --update ../sparql/inject-subset-declaration.ru --update ../sparql/inject-synonymtype-declaration.ru \
		remove $(patsubst %, --term %, $(ANNOTATION_PROPERTIES)) -T $(IMPORTDIR)/hp_terms_combined.txt --select complement --select "classes individuals annotation-properties" \
		remove --axioms Declaration \
		annotate --ontology-iri $(ONTBASE)/$@ $(ANNOTATE_ONTOLOGY_VERSION) --output $@.tmp.owl && mv $@.tmp.owl $@; fi
	

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

MERGE_TEMPLATE=tmp/merge_template.tsv
TEMPLATE_URL=NO_TEMPLATE_URL_PROVIDED

tmp/merge_template.tsv:
	wget "$(TEMPLATE_URL)" -O $@

merge_template: $(MERGE_TEMPLATE)
	$(ROBOT) template --merge-before --input $(SRC) \
 --template $(MERGE_TEMPLATE) convert -f ofn -o $(SRC)

tests_fast:
	$(MAKE_FAST) test


