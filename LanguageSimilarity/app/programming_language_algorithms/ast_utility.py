import ast
import io
import tokenize

def remove_comments(source: str) -> str:
    result = []
    tokens = tokenize.generate_tokens(io.StringIO(source).readline)

    for tok in tokens:
        tok_type, tok_string, start, end, line = tok
        if tok_type != tokenize.COMMENT:
            result.append(tok)

    return tokenize.untokenize(result)

def extract_tokens_from_ast(node):
    tokens = []

    def visit(node):
        if isinstance(node, ast.Constant):
            tokens.append(f"Const({repr(node.value)})")
        elif isinstance(node, ast.AST):
            if not(isinstance(node, ast.Module) or isinstance(node, ast.Load)):
                tokens.append(type(node).__name__)
            for child in ast.iter_child_nodes(node):
                visit(child)

    visit(node)
    return tokens


def parse_code_to_tokens(code: str):
    try:
        tree = ast.parse(code)
        return extract_tokens_from_ast(tree)
    except SyntaxError:
        return []