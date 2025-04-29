import spacy

nlp = spacy.load("en_core_web_lg") # python -m spacy download en_core_web_lg

def get_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)