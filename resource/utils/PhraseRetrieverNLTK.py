import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import defaultdict
from Evaluations_InitialDiagnosis import order_dictionary, dict_to_file

# for all grammars
grammars = []


def unusual_word(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    return sorted(text_vocab - english_vocab)


def remove_stopwords(text):
    """
    Remove all stop words from a sequence of words

    :param text:
    :return:
    """
    stop_words = stopwords.words('english')
    return [w.lower() for w in text if w not in stop_words]


def percent_non_stopwords(text):
    """
    Calculate the percent of words that are not stopwords

    Non alphabet words are regarded as stopwords.
    :param text:
    :return:
    """
    return len(remove_stopwords(text)) / len(text)


def is_synonym(word1, word2):
    """Test whether the first word is in the synset(s) of the second word"""
    for synset_word2 in wordnet.synsets(word2):
        if word1 in synset_word2.lemma_names():
            return True
    return False


def text_preprocess(document):
    """Preprocess a document for information retrieval

    For any given document, do the following three steps:
    1. segment the document into sentences
    2. tokenize each sentence
    3. tag each token

    @return: a list of sentences that are tokenized and tagged
    """
    sent_tokenized =[]
    for paragraph in document.split('\n'):
        if(paragraph.strip()):
            sentences = nltk.sent_tokenize(paragraph)
            for sens in sentences:
                sens = nltk.word_tokenize(sens)
                sent_tokenized.append(list(nltk.pos_tag(sens)))
    return sent_tokenized


def phrase_retrieval(grammar, sentence):
    """Retrieve phrases that match the grammar.

    eg. grammar = "NP: {<DT>?<JJ>*<NN>}" for noun phrase chunk
        grammar = "CHUNK: {<V.*> <TO> <V.*>}"

    @return: a tree representation
    """
    cp = nltk.RegexpParser(grammar)
    return cp.parse(sentence)


def subtree_string(tree, grammar, dict_default):
    """Extract the strings from extracted chunk. Return a dictionary."""
    for subtree in tree.subtrees():
        if subtree.label() == grammar.split(':')[0].strip():
            phrase = ' '.join([text for (text, tag) in subtree.leaves()])
            dict_default[phrase.lower()] += 1 # TODO: return a list of strings


def string_to_dict(string, dict_default):
    dict_default[string] += 1

def add_grammar(new_grammar):
    grammars.append(new_grammar)


def parseall(text_corpus, dict_default):
    for grammar in grammars:
        parse(text_corpus, grammar, dict_default)


def parse(text_corpus, new_grammar, dict_default):
    for ids in text_corpus.fileids():
        for sent in text_preprocess(text_corpus.raw(ids)):
            tree = phrase_retrieval(new_grammar, sent)
            subtree_string(tree, new_grammar, dict_default)





def main():
    # read in all text files
    corpus_root = '../Gene_Reviews_Extracted/Evaluations_Initial_Diagnosis'
    gene_reviews = PlaintextCorpusReader(corpus_root, '.*')
    extracted_phrases = defaultdict(int) # use it to save extracted phrases

    # define grammar for interested phrases
    grammar = "NP: {<JJ.*|DT>*<NN.*>*<IN|DT>*<NN.*><TO>}" # e.g. Evaluation of the palate to
    add_grammar(grammar)

    grammar = "NP: {<JJ.*|DT>*<NN.*>*<CC><JJ.*|DT>*<NN.*>*<TO>}"
    add_grammar(grammar)

    grammar = "VP: {<VB|VBJ><JJ.*|DT>*<NN.*><CC>*<JJ.*|DT>*<NN.*>*}"
    add_grammar(grammar)
    # just parse the most recent grammar
    #parse(gene_reviews, grammar, extracted_phrases)

    # parse with all grammars
    print(grammars)
    parseall(gene_reviews, extracted_phrases)
    extracted_phrases = order_dictionary(extracted_phrases)
    dict_to_file(extracted_phrases, '../auto_parse_NLTK.txt')


if __name__ == '__main__':
    main()
