from app.programming_language_algorithms.ast_utility import parse_code_to_tokens, remove_comments


def get_similarity(code1:str, code2:str)->float:
    tokens1 = parse_code_to_tokens(remove_comments(code1))
    tokens2 = parse_code_to_tokens(remove_comments(code2))

    common = sum(1 for a, b in zip(tokens1, tokens2) if a == b)
    max_len = max(len(tokens1), len(tokens2))
    return round(common / max_len, 4)