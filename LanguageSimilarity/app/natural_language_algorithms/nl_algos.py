from app.natural_language_algorithms import difflib_gestalt_pattern_matching as d_gpm
from app.natural_language_algorithms import gestalt_pattern_matching as gpm
from app.natural_language_algorithms import sklearn_vectorizer as s_vec
from app.natural_language_algorithms import spacy_nlp as s_nlp
from app.natural_language_algorithms import sentence_transformers_tensor as stt
from app.natural_language_algorithms import sentence_transformers_tensor_ua as stt_ua
from app.natural_language_algorithms import stanza_jaccard as sj
from app.natural_language_algorithms import fine_tuned_similarity_model as ft_sm

ALGOS = {
    "gestalt pattern matching": gpm.get_similarity,
    "gestalt pattern matching from difflib":d_gpm.get_similarity,
    "jaccard algorithm with stanza lematization":sj.get_similarity,
    "sklearn vectorizer":s_vec.get_similarity,
    "semantic similarity with spacy":s_nlp.get_similarity,
    "sentence transformers tensor with multilanguage vectors":stt.get_similarity,
    "sentence transformers tensor with ukrainian vectors":stt_ua.get_similarity,
    "fine tuned similarity model":ft_sm.get_similarity,
}