from __future__ import annotations
from yogi import read
from dataclasses import dataclass

@dataclass
class Node:
    data: int
    l: Tree
    r: Tree

Tree = Node | None

def lowest_common_ancestor_bst(T: Tree, x: int, y: int) -> int: 
    """Given a binary search tree T, returns de lowest(deepest) common ancestor between two nodesx and y."""
    # Strat: llegir en pre-ordre
    # Cas base
    if T is None:
        return -1
    
    if x <= T.data <= y:
        return T.data
    elif y < T.data:
        return lowest_common_ancestor_bst(T.l, x, y)
    return lowest_common_ancestor_bst(T.r, x, y)

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
            if x > y:
                x, y = y, x
            if x == y == -1:
                break
            print(lowest_common_ancestor_bst(T, x, y))
        print()


if __name__ == "__main__":
    main()