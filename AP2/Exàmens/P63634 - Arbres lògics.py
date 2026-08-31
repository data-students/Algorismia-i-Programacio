from __future__ import annotations
from dataclasses import dataclass
from typing import Iterator

# tags for nodes in the tree
LEAF = 0
NOT = 1
AND = 2
OR = 3

# nodes contain different informations according to their tag
@dataclass
class Node:
    tag: int  # can be LEAF, AND, OR, NOT
    lft: LogicTree = None  # when AND, OR, NOT
    rgt: LogicTree = None  # when AND, OR
    var: str = ""  # when LEAF

# logic trees are implemented with references to Node instances
LogicTree = Node | None

def build2(words: Iterator[str]) -> LogicTree:
    """Returns the logic tree corresponding to the logic expression in words"""
    key = next(words)
    if key == "NOT":
        return Node(NOT, build2(words))
    if key == "AND":
        return Node(AND, build2(words), build2(words))
    if key == "OR":
        return Node(OR, build2(words), build2(words))
    else:
        return Node(LEAF, var=key)


def build(expr: str) -> LogicTree:
    """Returns the logic tree corresponding to the logic expression in expr"""
    expr = expr.replace("(", " ")
    expr = expr.replace(")", " ")
    expr = expr.replace(",", " ")
    return build2(iter(expr.split()))

# writes a logic tree with some indentation
def write(tree: LogicTree, indent: str ="") -> None:

    assert tree is not None

    print(indent, end="")
    if tree.tag == LEAF:
        print(tree.var)
    elif tree.tag == NOT:
        print("NOT")
        write(tree.lft, indent + " ")
    else:
        print("AND" if tree.tag == AND else "OR")
        write(tree.lft, indent + " ")
        write(tree.rgt, indent + " ")

# evaluates tree with true variables in true_vars
def eval(tree: LogicTree, true_vars: set[str]) -> bool:

    assert tree is not None

    if tree.tag == LEAF:
        return tree.var in true_vars
    if tree.tag == NOT:
        return not eval(tree.lft, true_vars)
    if tree.tag == AND:
        return eval(tree.lft, true_vars) and eval(tree.rgt, true_vars)
    else:
        return eval(tree.lft, true_vars) or eval(tree.rgt, true_vars)

def main() -> None:
    # read an expression and build its tree
    expr  = input()
    tree = build(expr)

    # write the tree
    if tree is not None:
        write(tree)
    print("----------")

    # read assignments and write their evaluation
    try:
        while True:
            line = input()
            true_vars: set[str] = set()
            for var in line.split():
                true_vars.add(var)
            if eval(tree, true_vars):
                print("true")
            else:
                print("false")
    except EOFError:
        pass

if __name__ == "__main__":
    main()