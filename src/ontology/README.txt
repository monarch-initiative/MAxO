My method of creating ontologies modules

Goal: create medical action ontology with dosdp-tools and try to use existing ontologies as much as we can

Steps:

1. create yaml template
   need to define classes used in the pattern
   need to define relations used in the pattern
   need to add properties of the class with variables

   The following is an example:

pattern_name: avoid_consumption_of_foods
classes:
  avoidance of food: MAO:0020229
  food entity: FOODON:03411564 
  Thing: 'owl:Thing'
relations:
  has input: RO:0002352

annotationProperties:
  hasExactSynonym: oio:hasExactSynonym
  def: "oio:hasDefinition"
  reference: "oio:hasDbXref"

vars:
  food: "'food entity'"
  Xref: "'Thing'" #'Thing' means Xref ranges in everything

name:
  text: "avoid consumption of %s"
  vars:
    - food

annotations:
  - annotationProperty: hasExactSynonym
    text: "%s should be avoided"
    vars:
      - food

  - annotationProperty: def
    text: "A medical requirement of avoiding the consumption of %s. Negligence of the advice may interfere with disease treatment, prolong the recovery phase or even cause severe complications."
    vars:
      - food

  - annotationProperty: reference
    text: "refer to %s"
    vars:
      - Xref
  
equivalentTo:
  text: "'avoidance of food' and ('has input' some %s)"
  vars:
    - food


2. create a TSV file for the template
   there should be columns that correspond to variables used in the pattern
   
   At a minimal level, two columns are absolutely required: 
   defined_class and one variable ("food" in the following example). If food_label is not provided, we can specifiy reference ontology when running dosdp-tools so that we get the label from reference ontology. 

   The following is an example:

defined_class	food	food_label	Xref
MAO:0040001	FOODON:03411564	food source	
MAO:0040002	FOODON:03411297	animal used as food source	
MAO:0040003	FOODON:03411301	algae as food source	
MAO:0040004	FOODON:03411261	fungus as food source	
MAO:0040005	FOODON:03412345	lichen as food source	
MAO:0040006	FOODON:03412974	liquid as food source	
MAO:0040007	FOODON:03411347	plant used as food source	
MAO:0040008	FOODON:03412846	bacteria as food source	
MAO:0040009	FOODON:03411624	amphibian as food source	https://en.wikipedia.org/wiki/Amphibian
MAO:0040010	FOODON:03411134	animal (mammal) as food source	
MAO:0040011	FOODON:03411021	fish or lower water animal as food source	
MAO:0040012	FOODON:03411220	insect as food source	
MAO:0040013	FOODON:03411563	poultry or game bird as food source	
MAO:0040014	FOODON:03411625	reptile as food source	
MAO:0040015	FOODON:03411140	fruit-producing plant as food source	
MAO:0040016	FOODON:03411047	grain or seed-producing plant as food source	
MAO:0040017	FOODON:03413357	plant according to family as food source	
MAO:0040018	FOODON:03413359	plant for medicinal use as food source	
MAO:0040019	FOODON:03413358	plant used as fodder as food source	
MAO:0040020	FOODON:03414168	plant used for dietary supplements as food source	
MAO:0040021	FOODON:03411013	plant used for producing extract or concentrate as food source	
MAO:0040022	FOODON:03411179	spice or flavor-producing plant as food source	
MAO:0040023	FOODON:03411579	vegetable-producing plant as food source	
MAO:0040024	FOODON:03411252	frog as food source	


3. create a file that list the prefixes 
   one such file should be enough as long as it contains all prefixes

   The following is an example (just add more):

oio: 'http://www.geneontology.org/formats/oboInOwl#'



4. run dosdp-tools to generate a sub-ontology based on the pattern

   An example command line:

dosdp-tools generate --obo-prefixes=true --prefixes=../pattern/prefixes.yaml --template=../pattern/avoid_consumption_of_foods.yaml --infile=avoid_foods.tsv --ontology=../other_ontology/foodon-merged.owl --outfile=avoid_foods.owl

   If the input file is csv rather than TSV, add option "--table-format=csv"
   Option "ontology=foodon.owl" can provide labels for referenced terms. 

5. use robot to extract all terms (and related) referenced in the sub-ontology

   Use the tsv file, cut out the column for IDs of references (remove header) and then use it to extract. 
   cut -f 2 avoid_foods.tsv | sed '1d' > foods_terms.tsv

   robot extract --method BOT --input ../other_ontology/foodon-merged.owl --term-file foods_terms.tsv --output xfoodon.owl -p "FOODON:http://purl.obolibrary.org/obo/FOODON_"

   robot extract --method BOT --input ../other_ontology/ro.owl --term-file ro_terms.tsv --output xro.owl

   BOT and STAR both work; BOT pulls more. Is STAR enough? Need to read SLME theory to make a judgement.

6. merge the extracted terms with the sub-ontology
   
   run merge command to merge ref sub-ontology and the subontology generated from template into one.

robot merge --input avoid_foods.owl --input xfoodon.owl --input xro.owl --output avoid_foods-merged.owl

7. do reasoning to create class hiarachy 

   This can be done in Protege. What is the best way to do this?


8. remove external classes(?)

robot merge --input merged.owl unmerge --input subontology2.owl --output subtracted.owl 
