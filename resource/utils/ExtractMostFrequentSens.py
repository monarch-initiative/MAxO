import glob
from collections import OrderedDict
import re
import os
from XML_parser import disease_name, gene_NBKid
from exist_OtherOntology import Ontology, ontologies_has_query


def get_short_sentences(filepath, threshold, short_sentences):
    """
    Retrieve the most frequent sentences/phrases

    :param filepath: path to target file
    :param threshold: max number of words
    :param short_sentences: a dictionary for storing sentences and their number of appearance
    """
    for line in iter(open(filepath)):
        # replace all ';' and '.' to linebreaker so that they can be break into individual sentences
        for sentence in line.lower().replace(';', '\n').replace('.', '\n').split('\n'):
                # for each sentence, get the number of words; put words <= threshold to dictionary
            if sentence.strip() and len(sentence.strip()) > 2 and len(re.split('\W', sentence)) <= threshold:
                if sentence.strip() in short_sentences.keys():
                    short_sentences[sentence.strip()] = short_sentences[sentence.strip()] + 1
                else:
                    short_sentences[sentence.strip()] = 1

def get_short_sentences_and_origin(filepath, threshold, short_sentences, origin):
    """
    Retrieve the most frequent sentences/phrases and also record the origin.
    Similar to the above function, but keeps an additional record.
    The function has to use individual files instead of a combined file so that it can get the origin.

    :param filepath:
    :param threshold:
    :param short_sentences:
    :param origin:
    :return:
    """
    gene_NBKid_dict = gene_NBKid()  # get a dict that has gene symbol -> NBKid relationship

    for line in iter(open(filepath)):
        # replace all ';' and '.' to linebreaker so that they can be break into individual sentences
        for sentence in line.lower().replace(';', '\n').replace('.', '\n').split('\n'):
                # for each sentence, get the number of words; put words <= threshold to dictionary
            if sentence.strip() and len(sentence.strip()) > 2 and len(re.split('\W', sentence)) <= threshold:
                origin_disease = filepath.split('/')[-1].split('___')[-1]
                try:
                    origin_NBKid = gene_NBKid_dict[origin_disease.split('.txt')[0]]
                except KeyError:
                    print('no match is found for: ' + origin_disease.split('.txt')[0])
                if sentence.strip() in origin.keys():
                    short_sentences[sentence.strip()] = short_sentences[sentence.strip()] + 1
                    origin[sentence.strip()].append(origin_NBKid)
                else:
                    origin[sentence.strip()] = list([origin_NBKid])
                    short_sentences[sentence.strip()] = 1


def get_short_sentences_and_xref(filepath, threshold, short_sentences, xref):

    chebi = Ontology('../Other_ontologies/chebi.obo')
    hp = Ontology('../Other_ontologies/hp.obo')
    uberon = Ontology('../Other_ontologies/uberon.obo')
    ontologies = {'chebi': chebi,
                  'hp': hp,
                  'uberon': uberon}

    for line in iter(open(filepath)):
        # replace all ';' and '.' to linebreaker so that they can be break into individual sentences
        for sentence in line.lower().replace(';', '\n').replace('.', '\n').split('\n'):
                # for each sentence, get the number of words; put words <= threshold to dictionary
            if sentence.strip() and len(sentence.strip()) > 2 and len(re.split('\W', sentence)) <= threshold:
                if sentence.strip() in xref.keys():
                    short_sentences[sentence.strip()] = short_sentences[sentence.strip()] + 1
                else:
                    xref[sentence.strip()] = ontologies_has_query(ontologies, sentence.strip())
                    short_sentences[sentence.strip()] = 1

def dict_to_file(dict, path):
    """ Save a dictionary to a file

    :param dict: target dictionary
    :param path: where to save the file
    """
    with open(path, 'w') as file:
        for (k, v) in dict.items():
            file.write(str(k) + '\t' + str(v) + '\n')


def order_dictionary(dict):
    """
    Sort a dictionary based on the value (reverse)

    :param dict: unordered dictionary
    :return: ordered dictionary
    """
    return OrderedDict(sorted(dict.items(), key=lambda t: t[1], reverse=True))


def frequent_sentences(target, out, threshold=10):
    """
    Take a file as input, find the most frequent sentences (word account <= a threshold),
    save them and their frequency in the output file
    :param target: file to find frequent sentences
    :param out: output file
    :param threshold: maximal # of words to be considered a short sentence. Default is 10
    """
    short_sentences = {}
    get_short_sentences(target, threshold, short_sentences)
    most_frequent = order_dictionary(short_sentences)
    dict_to_file(most_frequent, out)

def frequent_sentences_and_origin(target_files, out, threshold=10):
    short_sentences = {}
    sentence_origin = {}
    for file in target_files:
        get_short_sentences_and_origin(file, threshold, short_sentences, sentence_origin)
    short_sentences = order_dictionary(short_sentences)
    with open(out, 'w') as outfile:
        for (k, v) in short_sentences.items():
            outfile.write('\t'.join([k, str(v), '|'.join(sentence_origin[k]), '\n']))

def frequent_sentences_and_xref(target_files, out, threshold=10):
    short_sentences = {}
    sentence_xref = {}
    for file in target_files:
        get_short_sentences_and_xref(file, threshold, short_sentences, sentence_xref)
    short_sentences = order_dictionary(short_sentences)
    with open(out, 'w') as outfile:
        for (k, v) in short_sentences.items():
            outfile.write('\t'.join([k, str(v), '|'.join(sentence_xref[k]), '\n']))



def frequent_sentences_all_management():
    """
        Get the most frequent sentences in the entire Management section
        Threshold is set at 10 words. Note: results not very good.

        :return: a text table with the most frequent sentences/phrases that are less than 10 words
        """
    short_sentences = {}
    target = '../management_all_disease.txt'
    threshold = 10
    get_short_sentences(target, threshold, short_sentences)
    most_freqent_10 = order_dictionary(short_sentences)
    dict_to_file(most_freqent_10, '../most_frequent_phrase_10_words_entire_management.txt')

def frequent_after_manual_parsing():
    short_sentences = {}
    target = '../manual_parse_Evaluation_initial_Diagnosis_all_disease.text'
    threshold = 10
    get_short_sentences(target, threshold, short_sentences)
    most_freqent_10 = order_dictionary(short_sentences)
    dict_to_file(most_freqent_10, '../most_frequent_phrase_10_words_initial_diagnosis_manual_parsing.txt')

def get_ontology_terms():
    # get the most frequent sentences (no more than 10 words) of each subsection of management
    target_files = glob.glob('../Gene_Reviews_Extracted/Sections_combined/*.txt')
    for target in target_files:
        out = ''.join(['../Ontology_Terms/Most_Frequent_Sens/most_frequent_10_', target.split('/')[-1]])
        frequent_sentences(target, out, threshold=10)

    # get the most frequent sentences (no more than 10 words) in the entire Management section
    target = '../management_all_disease.txt'
    out = '../Ontology_Terms/Most_Frequent_Sens/most_frequent_10_entire_management.txt'
    frequent_sentences(target, out, threshold=10)

    # get the most frequent sentences (no more than 10 words) in the entire Management section after some manual parsing
    target = '../manual_parse_Evaluation_initial_Diagnosis_all_disease.text'
    out = '../Ontology_Terms/Most_Frequent_Sens/most_frequent_10_Evaluations_Following_Initial_Diagnosis_all_diseases_manually_parsed.txt'
    frequent_sentences(target, out, threshold=10)

def get_ontology_terms_and_origin():
    try:
        os.mkdir('../Ontology_Terms/Most_Frequent_Sens_and_Origin')
    except FileExistsError:
        pass
    # get the most frequent sentences (no more than 10) of avoidance section
    """
    
    target_files = glob.glob('../Gene_Reviews_Extracted/Agents_Circumstances_to_Avoid/*.txt')
    out_folder = '../Ontology_Terms/Most_Frequent_Sens_and_Origin/most_frequent_10_'
    out_file = out_folder + 'Agents_Circumstances_to_Avoid' + '.txt'
    frequent_sentences_and_origin(target_files, out_file, threshold=10)
    """

    input_folders = ['Agents_Circumstances_to_Avoid', 'Evaluation_of_Relatives_at_Risk',
                     'Evaluations_Following_Initial_Diagnosis', 'Prevention_of_Primary_Manifestations',
                     'Prevention_of_Secondary_Complications', 'Surveillance', 'Treatment_of_Manifestations']
    out_folder = '../Ontology_Terms/Most_Frequent_Sens_and_Origin/'
    for input_folder in input_folders:
        target_files = glob.glob('../Gene_Reviews_Extracted/' + input_folder + '/*.txt')
        out_file = out_folder + 'most_frequent_10_' + input_folder + '.txt'
        frequent_sentences_and_origin(target_files, out_file, threshold=10)

    # get the most frequent sentences (no more than 10 words) in the entire Management section
    target = glob.glob('../Gene_Reviews_Extracted/*.txt')
    out = '../Ontology_Terms/Most_Frequent_Sens_and_Origin/most_frequent_10_entire_management.txt'
    frequent_sentences_and_origin(target, out, threshold=10)

    # get the most frequent sentences (no more than 10 words) in the entire Management section after some manual parsing
    target = ['../manual_parse_Evaluation_initial_Diagnosis_all_disease.text']
    print('Unalbe to find origin on manully parsed data')


def get_ontology_terms_and_xref():
    try:
        os.mkdir('../Ontology_Terms/Most_Frequent_Sens_and_Xref')
    except FileExistsError:
        pass
    # get the most frequent sentences (no more than 10) of avoidance section

    input_folders = ['Agents_Circumstances_to_Avoid', 'Evaluation_of_Relatives_at_Risk',
                     'Evaluations_Following_Initial_Diagnosis', 'Prevention_of_Primary_Manifestations',
                     'Prevention_of_Secondary_Complications', 'Surveillance', 'Treatment_of_Manifestations']
    out_folder = '../Ontology_Terms/Most_Frequent_Sens_and_Xref/'
    for input_folder in input_folders:
        target_files = glob.glob('../Gene_Reviews_Extracted/' + input_folder + '/*.txt')
        out_file = out_folder + 'most_frequent_10_' + input_folder + '.txt'
        frequent_sentences_and_xref(target_files, out_file, threshold=10)

    # get the most frequent sentences (no more than 10 words) in the entire Management section
    target = glob.glob('../Gene_Reviews_Extracted/*.txt')
    out = '../Ontology_Terms/Most_Frequent_Sens_and_Xref/most_frequent_10_entire_management.txt'
    frequent_sentences_and_xref(target, out, threshold=10)

    # get the most frequent sentences (no more than 10 words) in the entire Management section after some manual parsing
    target = ['../manual_parse_Evaluation_initial_Diagnosis_all_disease.text']
    print('Unalbe to find origin on manully parsed data')


if __name__ == '__main__':
    get_ontology_terms()
    get_ontology_terms_and_origin()
    #get_ontology_terms_and_xref() # too show to run
