from app.natural_language_algorithms import difflib_gestalt_pattern_matching as d_gpm
from app.natural_language_algorithms import jaccard_similarity as jac
from app.natural_language_algorithms import sklearn_vectorizer as s_vec

from app.natural_language_algorithms import spacy_semantic_similarity as sss
from app.natural_language_algorithms import multilingual_similarity_model as ml_sm
from app.natural_language_algorithms import ukr_multilingual_similarity_model as ukr_ml_sm
from app.natural_language_algorithms import scratch_similarity_model as sch_sm
from app.natural_language_algorithms import fine_tuned_similarity_model as ft_sm


ALGOS = {
    "gestalt pattern matching": d_gpm.get_similarity,
    "jaccard similarity": jac.get_similarity,
    "sklearn vectorizer": s_vec.get_similarity,

    "spacy semantic similarity": sss.get_similarity,
    "multilingual similarity model (paraphrase-multilingual-MiniLM-L12-v2)":ml_sm.get_similarity,
    "ukr Multilingual similarity model (ukr-paraphrase-multilingual-mpnet-base)":ukr_ml_sm.get_similarity,
    "scratch similarity model":sch_sm.get_similarity,
    "fine tuned similarity model (paraphrase-multilingual-MiniLM-L12-v2)":ft_sm.get_similarity,
}