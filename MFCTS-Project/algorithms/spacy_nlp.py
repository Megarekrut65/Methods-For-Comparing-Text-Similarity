import spacy

#ukranian vectors: https://fasttext.cc/docs/en/crawl-vectors.html
#convert for spacy: python -m spacy init vectors uk cc.uk.300.vec.gz ./uk_vectors

nlp = spacy.load("uk_vectors")

def get_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)