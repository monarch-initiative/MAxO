import re
from collections import OrderedDict


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

short_sentences = {}
filepath = '../Evaluation_initial_Diagnosis_all_disease.txt'
threshold = 10

get_short_sentences(filepath, threshold, short_sentences)

print(OrderedDict(sorted(short_sentences.items(), key = lambda t:t[1], reverse = True)))