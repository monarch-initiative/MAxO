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