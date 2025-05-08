import ast
import astor
import builtins

class RenameVariables(ast.NodeTransformer):
    def __init__(self):
        self.var_map = {}
        self.counter = 0
        self.builtin_names = set(dir(builtins))

    def _new_name(self):
        self.counter += 1
        return f"var{self.counter}"

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Load, ast.Store, ast.Del)):
            if (
                    node.id not in self.var_map and
                    not node.id.startswith("__") and
                    node.id not in self.builtin_names
            ):
                self.var_map[node.id] = self._new_name()
            node.id = self.var_map.get(node.id, node.id)
        return node

    def visit_FunctionDef(self, node):
        if (
                node.name not in self.var_map and
                not node.name.startswith("__") and
                node.name not in self.builtin_names
        ):
            self.var_map[node.name] = self._new_name()
        node.name = self.var_map.get(node.name, node.name)
        self.generic_visit(node)
        return node

def rename_code(code_str):
    try:
        tree = ast.parse(code_str)
        renamer = RenameVariables()
        new_tree = renamer.visit(tree)
        ast.fix_missing_locations(new_tree)
        return astor.to_source(new_tree)
    except Exception as e:
        print(f"Error parsing code: {e}")
        return code_str
