import glob
from collections import OrderedDict
import re


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
    for line in iter(open(filepath)):
        # replace all ';' and '.' to linebreaker so that they can be break into individual sentences
        for sentence in line.replace(';', '\n').replace('.', '\n').split('\n'):
                # for each sentence, get the number of words; put words <= threshold to dictionary
            if sentence.strip() and len(sentence.strip()) > 2 and len(re.split('\W', sentence)) <= threshold:
                if sentence.strip() in short_sentences.keys():
                    short_sentences[sentence.strip()] = short_sentences[sentence.strip()] + 1
                else:
                    short_sentences[sentence.strip()] = 1


def main():
    start_line = 'Evaluations Following Initial Diagnosis'
    end_line = 'Treatment of Manifestations'
    try:
        Evaluation_initial_Diagnosis = open('../Evaluation_initial_Diagnosis_all_disease.txt', 'w')
    except OSError:
        print('Cannot create file')
    all_files = glob.glob('../Gene_Reviews_Extracted/*.txt')
    for file in all_files:
        Evaluation_initial_Diagnosis.write(get_texts_between(file, start_line, end_line))
    Evaluation_initial_Diagnosis.close()

    short_sentences = {}
    filepath = '../Evaluation_initial_Diagnosis_all_disease.txt'
    threshold = 10
    get_short_sentences(filepath, threshold, short_sentences)
    most_freqent_10 = OrderedDict(sorted(short_sentences.items(), key=lambda t: t[1], reverse=True))
    try:
        most_frequent = open('../most_frequent_phrase_10_words.txt', 'w')
    except OSError:
        print('Cannot create file')
    for item in most_freqent_10:
        most_frequent.write(str(item) + '\t'+ str(most_freqent_10[item]) + '\n')
    most_frequent.close()


if __name__ == '__main__':
    main()