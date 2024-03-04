## Customize Makefile settings for maxo
## 
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile

#########################################
### Custom pipelines ####################
#########################################

# Will be available in ODK 1.5 (https://github.com/INCATools/ontology-development-kit/pull/803)

test: maxo-base.json

.PHONY: test
test_fast:
	$(MAKE_FAST) test

$(ONT)-base.owl: $(EDIT_PREPROCESSED) $(OTHER_SRC) $(IMPORT_FILES)
	$(ROBOT_RELEASE_IMPORT_MODE) \
	reason --reasoner ELK --equivalent-classes-allowed asserted-only --exclude-tautologies structural \
	relax \
	reduce -r ELK \
	remove --base-iri $(URIBASE)/MAXO_ --axioms external --preserve-structure false --trim false \
	$(SHARED_ROBOT_COMMANDS) \
	annotate --link-annotation http://purl.org/dc/elements/1.1/type http://purl.obolibrary.org/obo/IAO_8000001 \
		--ontology-iri $(ONTBASE)/$@ $(ANNOTATE_ONTOLOGY_VERSION) \
		--output $@.tmp.owl && mv $@.tmp.owl $@

#########################################
### Generating all ROBOT templates ######
#########################################

TEMPLATE_URL_MAXO=https://docs.google.com/spreadsheets/d/e/2PACX-1vTcCsupbjr3kEke__ymYi-JkAYoHhliC79FKBYALcQAcJNAwikJlNN5DcwzdAVqBFnj2-ix1cixKyv-/pub?gid=0&single=true&output=tsv

$(TEMPLATEDIR)/maxo-in-progress.tsv:
	wget "$(TEMPLATE_URL_MAXO)" -O $@

#########################################
### Custom import or mirror configs #####
#########################################

# Workaround for https://github.com/geneontology/obographs/issues/93. Basically removing all object properties since
# We cannot handle complex expressions in obographs in ODK 1.4

$(MIRRORDIR)/obi.owl: 
	if [ $(MIR) = true ]; then curl -L $(OBOBASE)/obi.owl --create-dirs -o $(MIRRORDIR)/obi.owl --retry 4 --max-time 200 &&\
		$(ROBOT) convert -i $(MIRRORDIR)/obi.owl -o $@.tmp.owl &&\
		$(ROBOT) remove -i $@.tmp.owl --base-iri $(URIBASE)/OBI --axioms external --preserve-structure false --trim false \
			remove --select object-properties -o $@.tmp.owl &&\
		mv $@.tmp.owl $@; fi

# Workaround for https://github.com/FoodOntology/foodon/pull/293
# Can be deleted after the next release of foodon
mirror-foodon: | $(TMPDIR)
	if [ $(MIR) = true ]; then curl -L $(OBOBASE)/foodon.owl --create-dirs -o $(MIRRORDIR)/foodon.owl --retry 4 --max-time 200 &&\
		$(ROBOT) convert -i $(MIRRORDIR)/foodon.owl -o $@.tmp.owl && \
		$(ROBOT) remove -i $@.tmp.owl --base-iri http://purl.obolibrary.org/obo/PO_ --base-iri http://purl.obolibrary.org/obo/FOODON_ --axioms external --preserve-structure false --trim false -o $@.tmp.owl &&\
		$(ROBOT) remove -i $@.tmp.owl --term "http://www.w3.org/1999/02/22-rdf-syntax-ns#type" -o $@.tmp.owl &&\
		mv $@.tmp.owl $(TMPDIR)/$@.owl; fi


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



##########################################
### Get maxo annotations            ######
##########################################
# YOU MUST SET THE MAXOA_RELEASE_PASSWORD ENVRIONMENTAL VARIABLE WHEN RELEASING
MAXOA_DIRECTORY=tmp/maxoa
MAXOA_FILENAME=maxo-annotations.tsv
MAXOA_RELEASE_PASSWORD=XXXXXXXFAKEPASSWORD

$(MAXOA_DIRECTORY)/$(MAXOA_FILENAME): $(SRC)
	mkdir -p $(MAXOA_DIRECTORY)
	@test $(MAXOA_RELEASE_PASSWORD)
	@curl -Lk https://poet.jax.org/api/v1/export/release?key=$(MAXOA_RELEASE_PASSWORD) && echo "POET Release Success!" || (echo "POET Release Failure." && exit 1)
	@curl -Lk https://poet.jax.org/api/v1/export/maxo >> $@

.PHONY: maxoa
maxoa:
	$(MAKE) $(MAXOA_DIRECTORY)/$(MAXOA_FILENAME)

prepare_release: maxoa

prepare_release_fast: maxoa

RELEASE_ASSETS_AFTER_RELEASE+= $(MAXOA_DIRECTORY)/$(MAXOA_FILENAME)

.PHONY: public_release
public_release:
	@test $(GHVERSION)
	ls -alt $(RELEASE_ASSETS_AFTER_RELEASE)
	gh release create $(GHVERSION) --title "$(VERSION) Release" --draft $(RELEASE_ASSETS_AFTER_RELEASE) --generate-notes


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

