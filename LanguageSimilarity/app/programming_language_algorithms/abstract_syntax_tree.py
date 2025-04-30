import ast

def get_similarity(code1:str, code2:str)->float:
    tree1 = list(ast.walk(ast.parse(code1)))
    tree2 = list(ast.walk(ast.parse(code2)))
    common = sum(1 for n1, n2 in zip(tree1, tree2) if type(n1) == type(n2))
    max_len = max(len(tree1), len(tree2))
    return round(common / max_len, 2)