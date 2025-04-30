import ast

def extract(code):
    return [type(node).__name__ for node in ast.walk(ast.parse(code))]

def get_similarity(code1:str, code2:str)->float:
    seq1 = extract(code1)
    seq2 = extract(code2)
    common = sum(1 for a, b in zip(seq1, seq2) if a == b)
    max_len = max(len(seq1), len(seq2))
    return round(common / max_len, 2)