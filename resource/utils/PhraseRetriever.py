import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import defaultdict
from ExtractMostFrequentSens import order_dictionary, dict_to_file


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
    sent_tokenized = []
    for paragraph in document.split('\n'):
        if (paragraph.strip()):
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
    """Extract strings from extracted chunk. Return a dictionary.

    @tree: a tree representation of tokenized sentences. Subtree contains chunks that have been extracted.
    @grammar: the grammar used to extract chunks. It is needed to identify target subtrees (chunks)
    @dict_default: a defaultdict where to put extracted phrases to
    """
    for subtree in tree.subtrees():
        if subtree.label() == grammar.split(':')[0].strip():
            phrase = ' '.join([text for (text, tag) in subtree.leaves()])
            dict_default[phrase.lower()] += 1


def parseall(text_corpus, grammars, dict_default):
    """Parse text corpus with all grammars that are defined, and export to a defaultdict"""
    for grammar in grammars:
        parse(text_corpus, grammar, dict_default)


def parse(text_corpus, new_grammar, dict_default):
    """Parse text corpus with one grammar, and export to a defaultdict"""
    for ids in text_corpus.fileids():
        for sent in text_preprocess(text_corpus.raw(ids)):
            tree = phrase_retrieval(new_grammar, sent)
            subtree_string(tree, new_grammar, dict_default)


class PhraseRetriever:
    def __init__(self, corpus):
        self.grammars = []
        self.corpus = corpus
        self.output = '../Ontology_Terms/NLTK_parsing/default_output.txt'

    def add_grammar(self, grammar):
        self.grammars.append(grammar)

    def add_grammars(self, grammars):
        self.grammars += grammars

    def get_grammars(self):
        return '\n'.join(self.grammars)

    def parse_test(self, grammar):
        test_dict = defaultdict(int)
        parse(self.corpus, grammar, test_dict)
        for (string, freq) in order_dictionary(test_dict).items():
            print(string, '\t', freq)

    def set_output(self, out):
        self.output = out

    def get_output(self):
        return self.output

    def parse_all(self):
        dict_default = defaultdict(int)
        for grammar in self.grammars:
            parse(self.corpus, grammar, dict_default)
        extracted_phrases = order_dictionary(dict_default)
        dict_to_file(extracted_phrases, self.output)


def parse_Avoidance():
    corpus_root = '../Gene_Reviews_Extracted/Agents_Circumstances_to_Avoid'
    gene_reviews_initial = PlaintextCorpusReader(corpus_root, '.*')
    phraseRetriever1 = PhraseRetriever(gene_reviews_initial)
    phraseRetriever1.set_output('../Ontology_Terms/NLTK_parsing/NLTK_Agents_Circumstances_to_Avoid.txt')

    grammars = ["NP: {<JJ.*|DT>*<NN.*>*<IN|DT>*<NN.*><TO>}",
                "NP: {<JJ.*|DT>*<NN.*>*<CC><JJ.*|DT>*<NN.*>*<TO>}",
                "VP: {<VB|NNJ><JJ.*|DT>*<NN.*><CC>*<JJ.*|DT>*<NN.*>*}"]  # e.g. Evaluation of the palate to

    phraseRetriever1.add_grammars(grammars)
    print(phraseRetriever1.get_grammars())
    # modify the following grammar for testing, use add_grammar(grammar) to export the list to file
    # grammar = "VP: {<VB><JJ.*>*<NN*>*<TO|IN><.*>*<JJ.*|DT>*<JJ>*<NN.*>}"
    # phraseRetriever1.parse_test(grammar)

    phraseRetriever1.parse_all()

def parse_Evaluations_Initial():
    corpus_root = '../Gene_Reviews_Extracted/Evaluations_Following_Initial_Diagnosis'
    gene_reviews_initial = PlaintextCorpusReader(corpus_root, '.*')
    phraseRetriever1 = PhraseRetriever(gene_reviews_initial)
    phraseRetriever1.set_output('../Ontology_Terms/NLTK_parsing/NLTK_Evaluations_Following_Initial_Diagnosis.txt')

    grammars = ["NP: {<JJ.*|DT>*<NN.*>*<IN|DT>*<NN.*><TO>}",
                "NP: {<JJ.*|DT>*<NN.*>*<CC><JJ.*|DT>*<NN.*>*<TO>}",
                "VP: {<VB|NNJ><JJ.*|DT>*<NN.*><CC>*<JJ.*|DT>*<NN.*>*}"]  # e.g. Evaluation of the palate to

    phraseRetriever1.add_grammars(grammars)
    print(phraseRetriever1.get_grammars())
    # modify the following grammar for testing, use add_grammar(grammar) to export the list to file
    # grammar = "VP: {<VB><JJ.*>*<NN*>*<TO|IN><.*>*<JJ.*|DT>*<JJ>*<NN.*>}"
    # phraseRetriever1.parse_test(grammar)

    phraseRetriever1.parse_all()

def parse_Prevention_Primary():
    corpus_root = '../Gene_Reviews_Extracted/Prevention_of_Primary_Manifestations'
    gene_reviews_initial = PlaintextCorpusReader(corpus_root, '.*')
    phraseRetriever1 = PhraseRetriever(gene_reviews_initial)
    phraseRetriever1.set_output('../Ontology_Terms/NLTK_parsing/NLTK_Prevention_of_Primary_Manifestations.txt')

    grammars = ["NP: {<JJ.*|DT>*<NN.*>*<IN|DT>*<NN.*><TO>}",
                "NP: {<JJ.*|DT>*<NN.*>*<CC><JJ.*|DT>*<NN.*>*<TO>}",
                "VP: {<VB|NNJ><JJ.*|DT>*<NN.*><CC>*<JJ.*|DT>*<NN.*>*}"]  # e.g. Evaluation of the palate to

    phraseRetriever1.add_grammars(grammars)
    print(phraseRetriever1.get_grammars())
    # modify the following grammar for testing, use add_grammar(grammar) to export the list to file
    # grammar = "VP: {<VB><JJ.*>*<NN*>*<TO|IN><.*>*<JJ.*|DT>*<JJ>*<NN.*>}"
    # phraseRetriever1.parse_test(grammar)

    phraseRetriever1.parse_all()

def parse_Prevention_Secondary():
    corpus_root = '../Gene_Reviews_Extracted/Prevention_of_Secondary_Complications'
    gene_reviews_initial = PlaintextCorpusReader(corpus_root, '.*')
    phraseRetriever1 = PhraseRetriever(gene_reviews_initial)
    phraseRetriever1.set_output('../Ontology_Terms/NLTK_parsing/NLTK_Prevention_of_Secondary_Complications.txt')

    grammars = ["NP: {<JJ.*|DT>*<NN.*>*<IN|DT>*<NN.*><TO>}",
                "NP: {<JJ.*|DT>*<NN.*>*<CC><JJ.*|DT>*<NN.*>*<TO>}",
                "VP: {<VB|NNJ><JJ.*|DT>*<NN.*><CC>*<JJ.*|DT>*<NN.*>*}"]  # e.g. Evaluation of the palate to

    phraseRetriever1.add_grammars(grammars)
    print(phraseRetriever1.get_grammars())
    # modify the following grammar for testing, use add_grammar(grammar) to export the list to file
    # grammar = "VP: {<VB><JJ.*>*<NN*>*<TO|IN><.*>*<JJ.*|DT>*<JJ>*<NN.*>}"
    # phraseRetriever1.parse_test(grammar)

    phraseRetriever1.parse_all()

def parse_Surveillance():
    corpus_root = '../Gene_Reviews_Extracted/Surveillance'
    gene_reviews_initial = PlaintextCorpusReader(corpus_root, '.*')
    phraseRetriever1 = PhraseRetriever(gene_reviews_initial)
    phraseRetriever1.set_output('../Ontology_Terms/NLTK_parsing/NLTK_Surveillance.txt')

    grammars = ["NP: {<JJ.*|DT>*<NN.*>*<IN|DT>*<NN.*><TO>}",
                "NP: {<JJ.*|DT>*<NN.*>*<CC><JJ.*|DT>*<NN.*>*<TO>}",
                "VP: {<VB|NNJ><JJ.*|DT>*<NN.*><CC>*<JJ.*|DT>*<NN.*>*}"]  # e.g. Evaluation of the palate to

    phraseRetriever1.add_grammars(grammars)
    print(phraseRetriever1.get_grammars())
    # modify the following grammar for testing, use add_grammar(grammar) to export the list to file
    # grammar = "VP: {<VB><JJ.*>*<NN*>*<TO|IN><.*>*<JJ.*|DT>*<JJ>*<NN.*>}"
    # phraseRetriever1.parse_test(grammar)

    phraseRetriever1.parse_all()

def parse_Treatment_Manifestations():
    corpus_root = '../Gene_Reviews_Extracted/Treatment_of_Manifestations'
    gene_reviews_initial = PlaintextCorpusReader(corpus_root, '.*')
    phraseRetriever1 = PhraseRetriever(gene_reviews_initial)
    phraseRetriever1.set_output('../Ontology_Terms/NLTK_parsing/NLTK_Treatment_of_Manifestations.txt')

    grammars = ["NP: {<JJ.*|DT>*<NN.*>*<IN|DT>*<NN.*><TO>}",
                "NP: {<JJ.*|DT>*<NN.*>*<CC><JJ.*|DT>*<NN.*>*<TO>}",
                "VP: {<VB|NNJ><JJ.*|DT>*<NN.*><CC>*<JJ.*|DT>*<NN.*>*}"]  # e.g. Evaluation of the palate to

    phraseRetriever1.add_grammars(grammars)
    print(phraseRetriever1.get_grammars())
    # modify the following grammar for testing, use add_grammar(grammar) to export the list to file
    # grammar = "VP: {<VB><JJ.*>*<NN*>*<TO|IN><.*>*<JJ.*|DT>*<JJ>*<NN.*>}"
    # phraseRetriever1.parse_test(grammar)

    phraseRetriever1.parse_all()



def main():
    parse_Avoidance()
    parse_Evaluations_Initial()
    parse_Prevention_Primary()
    parse_Prevention_Secondary()
    parse_Surveillance()
    parse_Treatment_Manifestations()

if __name__ == '__main__':
    main()
