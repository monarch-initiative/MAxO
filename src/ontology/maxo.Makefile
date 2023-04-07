## Customize Makefile settings for maxo
## 
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile

#########################################
### Custom pipelines ####################
#########################################

# Will be available in ODK 1.5 (https://github.com/INCATools/ontology-development-kit/pull/803)
.PHONY: test
test_fast:
	$(MAKE_FAST) test

#########################################
### Generating all ROBOT templates ######
#########################################

TEMPLATE_URL_MAXO=https://docs.google.com/spreadsheets/d/e/2PACX-1vTcCsupbjr3kEke__ymYi-JkAYoHhliC79FKBYALcQAcJNAwikJlNN5DcwzdAVqBFnj2-ix1cixKyv-/pub?gid=0&single=true&output=tsv

TEMPLATES=$(patsubst %.tsv, $(TEMPLATESDIR)/%.owl, $(notdir $(wildcard $(TEMPLATESDIR)/*.tsv)))

$(TEMPLATEDIR)/%.owl: $(TEMPLATEDIR)/%.tsv $(SRC)
	$(ROBOT) merge -i $(SRC) template --template $< --output $@ && \
	$(ROBOT) annotate --input $@ --ontology-iri $(ONTBASE)/components/$*.owl -o $@

$(TEMPLATEDIR)/maxo-in-progress.tsv:
	wget "$(TEMPLATE_URL_MAXO)" -O $@

templates: $(TEMPLATES)
	echo $(TEMPLATES)

#########################################
### Custom import or mirror configs #####
#########################################

# Workaround for https://github.com/geneontology/obographs/issues/93. Basically removing all object properties since
# We cannot handle complex expressions in obographs in ODK 1.4

$(MIRRORDIR)/obi.owl: 
	if [ $(MIR) = true ] && [ $(IMP) = true ]; then curl -L $(OBOBASE)/obi.owl --create-dirs -o $(MIRRORDIR)/obi.owl --retry 4 --max-time 200 &&\
		$(ROBOT) convert -i $(MIRRORDIR)/obi.owl -o $@.tmp.owl &&\
		$(ROBOT) remove -i $@.tmp.owl --base-iri $(URIBASE)/OBI --axioms external --preserve-structure false --trim false \
			remove --select object-properties -o $@.tmp.owl &&\
		mv $@.tmp.owl $@; fi

#########################################
### Custom Merge-Replace Pipeline  ######
#########################################

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

#########################################
### Merge template pipeline        ######
#########################################

MERGE_TEMPLATE=tmp/merge_template.tsv
TEMPLATE_URL=NO_TEMPLATE_URL_PROVIDED

tmp/merge_template.tsv:
	wget "$(TEMPLATE_URL)" -O $@

merge_template: $(MERGE_TEMPLATE)
	$(ROBOT) template --merge-before --input $(SRC) \
 --template $(MERGE_TEMPLATE) convert -f ofn -o $(SRC)


#########################################
### Graveyard        ####################
#########################################

# Delete this when you see this next time.
# tmp/remove.txt:
#	echo "HP:0025454" > $@
#	echo "HP:0012029" >> $@
#	echo "HP:0004360" >> $@
#	echo "HP:0032368" >> $@
#	echo "HP:0001941" >> $@
#	echo "HP:0032369" >> $@
#	echo "HP:0001948" >> $@
#	echo "HP:0040145" >> $@
#	echo "HP:0000843" >> $@
#	echo "HP:0000829" >> $@