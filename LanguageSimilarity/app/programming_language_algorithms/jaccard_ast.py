import ast

from app.programming_language_algorithms.ast_utility import parse_code_to_tokens, remove_comments


def get_similarity(code1: str, code2: str) -> float:
    tokens1 = set(parse_code_to_tokens(remove_comments(code1)))
    tokens2 = set(parse_code_to_tokens(remove_comments(code2)))

    intersection = tokens1 & tokens2
    union = tokens1 | tokens2
    if not union:
        return 1.0
    return round(len(intersection) / len(union), 4)