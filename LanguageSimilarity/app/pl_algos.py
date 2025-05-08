from app.programming_language_algorithms import gestalt_pattern_matching_ast as g_ast
from app.programming_language_algorithms import jaccard_ast as jac
from app.programming_language_algorithms import sequence_ast as seq
from app.programming_language_algorithms import zss_tree_edit_distance as zss_ted

from app.programming_language_algorithms import codebert_similarity_model as codebert_sm
from app.programming_language_algorithms import codet5_description_similarity as codet5_ds
from app.programming_language_algorithms import fine_tuned_codebert as ft_codebert


ALGOS = {
    "gestalt pattern matching with ast": g_ast.get_similarity,
    "jaccard similarity with ast": jac.get_similarity,
    "sequence matching with ast": seq.get_similarity,
    "tree edit distance": zss_ted.get_similarity,
    "codebert model cos similarity": codebert_sm.get_similarity,
    "codet5 description similarity": codet5_ds.get_similarity,
    "fine tuned codebert": ft_codebert.get_similarity,

}