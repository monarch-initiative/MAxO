import obonet
import networkx
import os
import glob


class Ontology:
    def __init__(self, path):
        self.ontology = obonet.read_obo(path)
        self.id_to_name = {}
        for id_, data in self.ontology.nodes(data=True):
            try:
                self.id_to_name[id_] = data['name'].lower()
            except KeyError:
                pass

    def get_classes(self):
        return self.id_to_name

    def print_classes(self):
        for (k, v) in self.id_to_name.items():
            print(k + '\t' + v)

    def is_exist(self, query):
        result = query.lower() in self.id_to_name.values()
        #print(query + " exists: " + str(result))
        return result


def ontologies_has_query(ontologies, query):
    has_query = []
    for (k, v) in ontologies.items():
        if v.is_exist(query):
            has_query.append(k)
    if len(has_query) > 0:
        return '|'.join(has_query)
    else:
        return ''


def main():
    chebi = Ontology('../Other_ontologies/chebi.obo')
    hp = Ontology('../Other_ontologies/hp.obo')
    uberon = Ontology('../Other_ontologies/uberon.obo')

    ontologies = {'chebi': chebi,
                  'hp': hp,
                  'uberon': uberon}

    query_files = glob.glob('../Ontology_Terms/Most_Frequent_Sens/*.txt')
    for query_file in query_files:
        destin_file_path = '../Ontology_Terms/Most_Frequent_Sens_and_Xref/' + query_file.split('/')[-1]
        destin_file = open(destin_file_path, 'w')
        for lines in open(query_file, 'r').readlines():
            query = lines.split('\t')[0]
            destin_file.write(query + '\t' + ontologies_has_query(ontologies, query) + '\n')
        destin_file.close()
if __name__ == '__main__':
    main()

"""
 
    
try:
    os.mkdir('../Ontology_Terms/Most_Frequent_Sens_and_Xref')
except FileExistsError:
    pass

origin_folder = '../Ontology_Terms/Most_Frequent_Sens_and_Origin/'
destin_folder = '../Ontology_Terms/Most_Frequent_Sens_and_Xref/'
origin_files = glob.glob(origin_folder + '.txt')



"""