from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("microsoft/codebert-base")

def get_similarity(text1, text2):
    embeddings = model.encode([text1, text2], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1])
    return float(score[0])