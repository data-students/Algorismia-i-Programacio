from __future__ import annotations
from yogi import read
from dataclasses import dataclass

@dataclass
class Node:
    data: int
    l: Tree
    r: Tree

Tree = Node | None

def lowest_common_ancestor(T: Tree, x: int, y: int, depth: int = 0) -> tuple[int, int] | None: # tuple[depth, node]
    """Given a binary tree T, returns de lowest(deepest) common ancestor between two nodesx and y."""
    # Strat: llegir en pre-ordre
    # Cas base
    if T is None:
        return None
    if T.data == x or T.data == y:
        return depth, T.data
    
    # Cas recursiu
    lca_l = lowest_common_ancestor(T.l, x, y, depth + 1)
    lca_r = lowest_common_ancestor(T.r, x, y, depth + 1)

    if lca_l and lca_r: 
        return depth, T.data
    return lca_l or lca_r


def read_tree() -> Tree:
    data = read(int)
    if data == -1:
        return None
    return Node(data, read_tree(), read_tree())
    

def main() -> None:
    k = read(int)
    for _ in range(k):
        T = read_tree()
        while True:
            x, y = read(int), read(int)
            if x == y == -1:
                break
            lca = lowest_common_ancestor(T, x, y)
            if lca is not None:
                print(lca[1])
        print()


if __name__ == "__main__":
    main()