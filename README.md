# Medical Action Ontology (MAXO)


The Medical Action Ontology (MAxO) provides a broad view of medical actions and includes terms for medical procedures, interventions, therapies, treatments, and recommendations.

# Top-level: 

Below are the top-level classes in MAxO and examples of each class. 

    **Palliative care**: 
        - end-of-life care
        - pain management
        - Etc.
    **Diagnostic procedure**: 
        - Biomarker analysis
        - Clinical imaging procedure
        - Clinical laboratory procedure
        - Etc.
    **Preventative therapeutics**: 
        - smoking prevention
        - preventative immunization
        - prevention of abnormal physiologic state, i.e., hypertension prevention
        - ketosis prevention
        - Etc.
    **Complementary and alternative therapies**: 
        - Acupuncture therapy
        - Chiropractic therapy
        - Etc.
    **Therapeutic procedure**: 
        - Biologic therapy
        - Pharmacotherapy
        - Physical therapy
        - Radiation therapy
        - Surgical procedure
        - Etc.
    **Medical action avoidance**:
        - ketogenic diet intake avoidance
        - avoid CT scan
        - radiograph imaging avoidance
        - Etc.

## Term inclusion: 

    - Process and not information entities are included. 
	Examples: clinical tests (yes), clinical results (no) 
		
    - Recommendations for diagnostics, therapy, treatment, or prevention or avoidance. Life skills would not be included, but it will be decided on a case by case basis.
	Examples: hearing aid usage and speech therapy (yes), sign language (no)
		
    - Clinical tests, examinations, and clinically relevant biomarker assessments will be included, but developmental research will not. Think CLIA certified tests.
	Examples: Clinical tests (yes), purely research lab tests (no)
		
    - Supplementation or alternative therapies are only included if there are studies indicating their utility and have been recommended in the clinical literature. This section will be kept minimal and decided on a case by case basis.
	Examples: chiropractic therapy, amino acid/vitamin supplementation(yes), herbal supplementation(no)-* 


## OBO ontologies imported

Below are the imported ontologies used for logical definitions

- [NBO](https://github.com/obo-behavior/behavior-ontology)
- [FOODON](https://github.com/FoodOntology/foodon)
- [CHEBI](https://github.com/ebi-chebi/ChEBI)
- [MAXO](https://github.com/monarch-initiative/MAxO)
- [HP](https://github.com/obophenotype/human-phenotype-ontology/issues)
- [UBERON](https://github.com/obophenotype/uberon)
- PR
- RO
- IAO
- [GO](https://github.com/geneontology/)
- [OBI](https://github.com/obi-ontology/obi)
        
        
### MAxO Curation

- DOSDP templates are the prefered method to add terms to MAxO as it coordinates term labels, textual definitions, and logical definitions. Manual and or Robot templates may be used, but please look first to see if DOSDP templates are in use. To learn more about how to develop and use DOSDP templates, see  [MAxOs DOSDP templates](https://github.com/monarch-initiative/MAxO/tree/master/src/patterns) wiki or [OBO DOSDP tutorials ](https://oboacademy.github.io/obook/tutorial/dosdp-overview/) for how to construct these).

- Manual additions via Protege
    
- ROBOT templates (see [MAxO ROBOT templates ](https://github.com/monarch-initiative/MAxO/tree/master/src/templates


### MAxO Governance

Request terms:

**GitHub tickets**
        - To request, edit, or correct a term,  create a MAxO [GitHub ticket](https://github.com/monarch-initiative/MAxO/issues). 
        - The more detail, including definition, synonyms, and axiomatization, the quicker the term will be added. 
        - Even better, add additional terms and children terms that are missing.
        - Overachiever? Group terms that have similarities might be grouped into (new) DOSDP patterns
**Pull requests**
    - If you are familiar with GitHub PRs and Protege, DOSDP, or ROBOT templates, then a person may create a pull request with your term.
    - PLEASE NOTE: <span style="text-decoration:underline;">DOSDP patterns</span>
        - Some terms are grouped together and created by DOSDP patterns 
        - If you know how to use DOSDP patterns, you can suggest adding a new pattern [HERE](https://github.com/monarch-initiative/MAxO/tree/master/src/patterns/dosdp-patterns) or a new term [HERE](https://github.com/monarch-initiative/MAxO/tree/master/src/patterns/data/manual).
    - For MAxO IDs: If unsure, leave blank or obtain from [HERE](https://github.com/monarch-initiative/MAxO/blob/master/src/patterns/data/todo/MAXO_availableIDs.txt)  (and then delete to signify using the ID) or request IDs from @LCCarmody.  
        - If still unsure, just use an ID number and the IDs will be changed upon PR review.
    - Tag @LCCarmody for review.

[MAxO GitHub Wiki](https://github.com/monarch-initiative/MAxO/wiki): Please use this as a ‘how to’ guide for editing MAxO
            

# License


MAxO is available under [CC-BY 4.0](LICENSE)

![CC BY 4.0](https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png "CC-BY 4.0")


# Project Homepage

 Future home: https://hpo.jax.org/
 
# CONTACT

### Tickets/Questions/Requests

Please post issues at our [github tracker.](https://github.com/monarch-initiative/MAxO/issues)

### Direct

 If you have questions, please contact leigh.carmody *at* jax.org or peter.robinson *at* jax.org

### Mailing list

If you would like email updates for releases medical-action-ontology-mailing-list@googlegroups.com


# Annotations

MAxO will provide a vocabulary to annotate diseases and phenotypes with recommended treatments and interventions. To make requests for annotations, please make a ticket here: https://github.com/monarch-initiative/maxo-annotations
If you would like to help making annotations or obtain a tsv file of annotations, request a login at https://poet.jax.org/


### Ontology use in practice

The goal is to focus on the computational representation of rare disease treatments and interventions. 

1. MAxO terms are currently being used to annotate disease and disease phenotypes using POET. [https://poet.jax.org/](https://poet.jax.org/-)

2. Clinical Centre of Expertise for Rare and Undiagnosed Diseases (Rare Care Centre) is using MAxO to annotate their work.

    FUTURE USE

3. Mining terms/identifying terms from [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1116/)–we have built text mining code to identify MAxO terms in Gene Reviews.

4. [Treatabolome](https://treatabolome.cnag.crg.eu/#/): A gene and variant-centric database of treatments for rare disease. Currently, team uses HPO terms for annotation.

