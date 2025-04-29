import stanza


stanza.download("uk")
nlp = stanza.Pipeline(lang="uk", processors="tokenize,mwt,pos,lemma")


def lemmatize(text):
    doc = nlp(text)
    return [word.lemma.lower() for sent in doc.sentences for word in sent.words]


def get_similarity(set1, set2):
    intersection = set(set1).intersection(set(set2))
    union = set(set1).union(set(set2))
    if not union:
        return 0.0
    return len(intersection) / len(union)