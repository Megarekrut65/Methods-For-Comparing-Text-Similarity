from sklearn.feature_extraction.text import TfidfVectorizer # https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return similarity_matrix[0][0]