import ast
from zss import simple_distance, Node

IGNORED_NODE_TYPES = {"Load", "Store", "Del", "Param", "ExprContext"}

class ASTNode(Node):
    def __init__(self, node):
        self.node = node
        self.node_type = type(node).__name__
        if isinstance(node, ast.Name):
            self.value = "Var"
        elif isinstance(node, ast.Constant):
            self.value = f"{repr(node.value)}"
        elif isinstance(node, ast.BinOp):
            self.value = node.op.__class__.__name__
        else:
            self.value = None


        label = f"{self.node_type}:{self.value}" if self.value is not None else self.node_type
        super().__init__(label)


def ast_to_zss(node):
    if type(node).__name__ in IGNORED_NODE_TYPES:
        return None

    root = ASTNode(node)

    for child in ast.iter_child_nodes(node):
        child_node = ast_to_zss(child)
        if child_node is not None:
            root.addkid(child_node)
    return root

def count_nodes(zss_node):
    count = 1
    for child in zss_node.children:
        count += count_nodes(child)
    return count


def get_similarity(code1, code2):
    tree1 = ast.parse(code1)
    tree2 = ast.parse(code2)

    zss_tree1 = ast_to_zss(tree1)
    zss_tree2 = ast_to_zss(tree2)
    size1 = count_nodes(zss_tree1)
    size2 = count_nodes(zss_tree2)
    max_size = max(size1, size2)

    distance = simple_distance(zss_tree1, zss_tree2 )

    return  1 - (distance / max_size) if max_size > 0 else 1.0
