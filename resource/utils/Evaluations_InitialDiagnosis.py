import glob
from collections import OrderedDict
import re
import os
from XML_parser import disease_name


def get_texts_between(filepath, start_line, end_line):
    """
    Extract text between two lines

    :param filepath: path to the target file
    :param start_line: starting line (exclusive)
    :param end_line: ending line (exclusive)
    :return: lines between the starting line and ending line (exclusive)
    """
    management = open(filepath)
    evaluation_initial_diagonosis = []
    in_range = False
    for line in iter(management):
        if line.strip() == start_line.strip():
            in_range = True
        if line.strip() == end_line.strip():
            break
        # remove empty lines and starting lines
        if in_range and line.strip() != start_line and line.strip():
            evaluation_initial_diagonosis.append(line)
    management.close()
    return '\n'.join(evaluation_initial_diagonosis)

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


def frequent_sentences_initial_diagnosis():
    """
    Get the most frequent sentences in "Evaluation following Initial Diagnosis"
    Threshold is set at 10 words.

    :return: a text table with the most frequent sentences/phrases that are less than 10 words
    """
    start_line = 'Evaluations Following Initial Diagnosis'
    end_line = 'Treatment of Manifestations'
    path_evaluation_initial_diagnosis = '../Evaluation_initial_Diagnosis_all_disease.txt'
    try:
        Evaluation_initial_Diagnosis = open(path_evaluation_initial_diagnosis, 'w')
    except OSError:
        print('Cannot create file')
    all_files = glob.glob('../Gene_Reviews_Extracted/*.txt')
    for file in all_files:
        Evaluation_initial_Diagnosis.write(get_texts_between(file, start_line, end_line))
    Evaluation_initial_Diagnosis.close()


    short_sentences = {}
    target = '../Evaluation_initial_Diagnosis_all_disease.txt'
    threshold = 15
    get_short_sentences(target, threshold, short_sentences)
    most_freqent_10 = order_dictionary(short_sentences)
    dict_to_file(most_freqent_10, '../most_frequent_phrase_15_words_initial_diagnosis.txt')

def section_initial_diagnosis():
    """
    Save the paragraph Evaluations Following Initial Diagnosis into individual files.

    """
    start_line = 'Evaluations Following Initial Diagnosis'
    end_line = 'Treatment of Manifestations'
    folder = '../Gene_Reviews_Extracted/Evaluations_Initial_Diagnosis/'
    all_files = glob.glob('../Gene_Reviews_Extracted/*.txt')
    for file in all_files:
        try:
            path_evaluation_initial_diagnosis = ''.join([folder, 'initial_', disease_name(file), '.txt'])
            Evaluation_initial_Diagnosis = open(path_evaluation_initial_diagnosis, 'w')
        except OSError:
            print('Cannot create file')
        Evaluation_initial_Diagnosis.write(get_texts_between(file, start_line, end_line))
        Evaluation_initial_Diagnosis.close()

def frequent_sentences_all_management():
    """
        Get the most frequent sentences in the entire Management section
        Threshold is set at 10 words. Note: results not very good.

        :return: a text table with the most frequent sentences/phrases that are less than 10 words
        """
    start_line = 'Management'
    end_line = '++++++++++++++++++++++++++++++++++++'

    try:
        entire_management = open('../management_all_disease.txt', 'w')
    except OSError:
        print('Cannot create file')
    all_files = glob.glob('../Gene_Reviews_Extracted/*.txt')
    for file in all_files:
        entire_management.write(get_texts_between(file, start_line, end_line))
    entire_management.close()

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
    frequent_sentences_initial_diagnosis()
    #frequent_sentences_all_management()
    frequent_after_manual_parsing()
    section_initial_diagnosis()