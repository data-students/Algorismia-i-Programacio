from __future__ import annotations
from yogi import read
from dataclasses import dataclass
from typing import Iterator

@dataclass
class Node:
    data: str
    l: BinTree
    r: BinTree
    pos: int = 0

BinTree = Node | None


def calc_pos_inorder(T: BinTree, matrix: list[list[str]],
                    level: int = 0, counter: int = 0) -> int:
    if T:
        counter = calc_pos_inorder(T.l, matrix, level + 1, counter)

        matrix[level][counter] = T.data
        
        counter += 1
        counter = calc_pos_inorder(T.r, matrix, level + 1, counter)

    return counter

def write_inorder(T: BinTree, matrix: list[list[str]]) -> None:
    calc_pos_inorder(T, matrix)
    for row in matrix:
        print(*row, sep="")

def read_preorder(ipt: Iterator[str], width_tree: int = 0, depth_tree: int = 0) -> tuple[BinTree, int, int]:
    data = next(ipt)
    if data != "-":
        left, w_l, d_l = read_preorder(ipt, depth_tree=depth_tree + 1)
        right, w_r, d_r = read_preorder(ipt, depth_tree=depth_tree + 1)
        return Node(data, left, right), w_r + w_l + 1, max(depth_tree, d_l, d_r)
    return None, width_tree, depth_tree

def main() -> None:
    n = read(int)
    for _ in range(n):
        ipt = iter(read(str))
        bin_tree, witdh_tree, depth_tree = read_preorder(ipt)
        if bin_tree:
            matrix = [["." for _ in range(witdh_tree)] for _ in range(depth_tree)]
            write_inorder(bin_tree, matrix)
        
        print()

if __name__ == "__main__":
    main()