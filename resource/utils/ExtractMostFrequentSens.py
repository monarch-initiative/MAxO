import glob
from collections import OrderedDict
import re
import os
from XML_parser import disease_name


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


def dict_to_file(dict, path):
    """ Save a dictionary to a file

    :param dict: target dictionary
    :param path: where to save the file
    """
    try:
        file = open(path, 'w')
    except OSError:
        print('Cannot create file')
    for item in dict:
        file.write(str(item) + '\t' + str(dict[item]) + '\n')
    file.close()


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

if __name__ == '__main__':
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