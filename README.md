# Medical Action Ontology (MAXO)

The Medical Action Ontology (MAxO) provides a structured vocabulary for medical procedures, interventions, therapies, and treatments. 

# Annotations

MAxO will provide a vocabulary to annotate diseases and phenotypes with recommended treatments and interventions. The Annotation repository is available here: https://github.com/monarch-initiative/maxo-annotations

# License


MAxO is available under [CC-BY 4.0](LICENSE)

![CC BY 4.0](https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png "CC-BY 4.0")


# Project Homepage

 Future home: https://hpo.jax.org/app/
 
# Questions/Requests/Tickets

 Please post issues at our github tracker. https://github.com/monarch-initiative/MAxO/issues

### Direct

 If you have questions, please contact leigh.carmody@jax.org or peter.robinson@jax.org

### Mailing list

If you would like email updates for releases medical-action-ontology-mailing-list@googlegroups.com


# **Medical Action Ontology (MAxO)**


### **Scope**[¶](https://oboacademy.github.io/obook/howto/ontology-overview/#scope)



* The Medical Action Ontology (MAxO) provides a <span style="text-decoration:underline;">broad</span> view of medical actions and includes terms for medical procedures, interventions, therapies, treatments, and recommendations.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")




* Top-level: <span style="text-decoration:underline;">complementary and alternative medical therapy</span>, <span style="text-decoration:underline;">diagnostic procedure</span>, <span style="text-decoration:underline;">medical action avoidance</span>, <span style="text-decoration:underline;">palliative care,</span> <span style="text-decoration:underline;">preventative therapeutics</span>, and <span style="text-decoration:underline;">therapeutic procedure</span>
    * <span style="text-decoration:underline;">Palliative care</span>: Examples: 
        * end-of-life care
        * pain management
        * Etc.
    * <span style="text-decoration:underline;">Diagnostic procedure</span>: 
        * Biomarker analysis
        * Clinical imaging procedure
        * Clinical laboratory procedure
        * Etc.
    * <span style="text-decoration:underline;">Preventative therapeutics</span>: 
        * smoking prevention
        * preventative immunization
        * prevention of abnormal physiologic state, i.e., hypertension prevention
        * ketosis prevention
        * Etc.
    * <span style="text-decoration:underline;">Complementary and alternative therapies</span>: 
        * Acupuncture therapy
        * Chiropractic therapy
        * etc.
    * <span style="text-decoration:underline;">Therapeutic procedure</span>: 
        * Biologic therapy
        * Pharmacotherapy
        * Physical therapy
        * Radiation therapy
        * Surgical procedure
    * <span style="text-decoration:underline;">Medical action avoidance</span>: 
        * ketogenic diet intake avoidance
        * avoid CT scan
        * radiograph imaging avoidance

Medical Action Ontology term inclusion: 



    * Medical recommendations: Ex. hearing aid usage and speech therapy (yes), sign language (no)
    * Process entities and not information entities: Lab tests (yes), lab research results (no) 
    * Clinical tests (yes), purely research lab tests (no)
    * Therapeutic supplementation (yes), alternative supplements (no)** 
* OBO ontologies are used for constructing logical definitions including:
        * [NBO ](https://github.com/obo-behavior/behavior-ontology)
        * [FOODON](https://github.com/FoodOntology/foodon)
        * [CHEBI](https://github.com/ebi-chebi/ChEBI)
        * [MAXO](https://github.com/monarch-initiative/MAxO)
        * [HP](https://github.com/obophenotype/human-phenotype-ontology/issues)
        * [UBERON](https://github.com/obophenotype/uberon)
        * PR
        * RO
        * IAO
        * [GO](https://github.com/geneontology/)
        * [OBI](https://github.com/obi-ontology/obi)

**Curation and governance workflows**[¶](https://oboacademy.github.io/obook/howto/ontology-overview/#curation-and-governance-workflows)


### MAxO Curation[¶](https://oboacademy.github.io/obook/howto/ontology-overview/#ontology-curation)



* PREFERRED METHOD:  DOSDP templates (see  [MAxOs DOSDP templates](https://github.com/monarch-initiative/MAxO/tree/master/src/patterns) wiki or [OBO DOSDP tutorials ](https://oboacademy.github.io/obook/tutorial/dosdp-overview/) for how to construct these)
    * DOSDP Pattern found [HERE](https://github.com/monarch-initiative/MAxO/tree/master/src/patterns/dosdp-patterns) in MAxO repo: 



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")




    * Example TSV: 



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")




* Manual additions via Protege (see [OBO tutorial](https://oboacademy.github.io/obook/howto/set-up-protege/#:~:text=General-,Protege,-ODK)<span style="text-decoration:underline;">)</span>
* ROBOT templates (see [MAxO ROBOT templates ](https://github.com/monarch-initiative/MAxO/tree/master/src/templates)and [OBO ROBOT tutorials](https://oboacademy.github.io/obook/reference/troublehooting-robot/#:~:text=Ontology-,Pipelines,-%2D%20ODK%2C%20ROBOT%2C%20etc))


### MAxO Governance [¶](https://oboacademy.github.io/obook/howto/ontology-overview/#governance)

 Request terms:



    * GitHub tickets
        * To request, edit, or correct a term,  create a MAxO [GitHub ticket](https://github.com/monarch-initiative/MAxO/issues). 
        * The more detail, including definition, synonyms, and axiomatization, the quicker the term will be added. 
        * Even better, add additional terms and children terms that are missing.
        * Overachiever? Group terms that have similarities might be grouped into (new) DOSDP patterns
* Pull requests
    * If you are familiar with GitHub PRs and Protege, DOSDP, or ROBOT templates, then a person may create a pull request with your term.
    * PLEASE NOTE: <span style="text-decoration:underline;">DOSDP patterns</span>
        * Some terms are grouped together and created by DOSDP patterns 
        * If you know how to use DOSDP patterns, you can suggest adding a new pattern [HERE](https://github.com/monarch-initiative/MAxO/tree/master/src/patterns/dosdp-patterns) or a new term [HERE](https://github.com/monarch-initiative/MAxO/tree/master/src/patterns/data/manual).
    * For MAxO IDs: If unsure, leave blank or obtain from [HERE](https://github.com/monarch-initiative/MAxO/blob/master/src/patterns/data/todo/MAXO_availableIDs.txt)  (and then delete to signify using the ID) or request IDs from @LCCarmody.  
        * If still unsure, just use an ID number and the IDs will be changed upon PR review.
    * Tag @LCCarmody for review.

            [MAxO GitHub Wiki](https://github.com/monarch-initiative/MAxO/wiki): Please use this as a ‘how to’ guide for editing MAxO



### **Ontology use in practice[¶](https://oboacademy.github.io/obook/howto/ontology-overview/#how-the-ontology-used-in-practice):**

The goal is to focus on the computational representation of rare disease treatments and interventions. Example:



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.jpg "image_tooltip")




1. MAxO terms are currently being used to annotate disease and disease phenotypes using POET. [https://poet.jax.org/](https://poet.jax.org/*)

<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")

2. Clinical Centre of Expertise for Rare and Undiagnosed Diseases (Rare Care Centre) is using MAxO to annotate their work.

    FUTURE USE

3. Mining terms/identifying terms from [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1116/)–we have built text mining code and are still in the developmental stage–brought code up to date, dealt with retired gene reviews
4. [Treatabolome](https://treatabolome.cnag.crg.eu/#/): A gene and variant-centric database of treatments for rare disease
