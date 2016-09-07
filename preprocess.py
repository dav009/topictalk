import nltk
from nltk.tree import Tree
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

p_stemmer = PorterStemmer()
english_stopwords = stopwords.words("english")

def get_continuous_chunks(chunk):
    current_chunk = []
    continuous_chunk = []
    for i in chunk:
            if type(i) == Tree:
                    current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                    named_entity = " ".join(current_chunk)
                    if named_entity not in continuous_chunk:
                            continuous_chunk.append(named_entity)
                            current_chunk = []
            else:
                    continue
    return continuous_chunk

def tokenize_and_stem_text(text):
    words = list()
    for sentence in nltk.sent_tokenize(text):
        for word in nltk.word_tokenize(sentence):
            if len(word)> 2 and word.lower() not in english_stopwords:
                words.append(p_stemmer.stem(word.lower()))
    return words