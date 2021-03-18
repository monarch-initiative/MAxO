#create robot template
sed $'2i\\\nID\t\t\tA obo:IAO_0000115\t>A oboInOwl:hasDbXref\n' maxo_ncit_def.tsv > merge_ncit_def.tsv
sed $'2i\\\nID\tA oboInOwl:IAO_0000115\t>A oio:hasDbXref\t\t\n' maxo_ncit_def.tsv > unmerge_ncit_def.tsv
