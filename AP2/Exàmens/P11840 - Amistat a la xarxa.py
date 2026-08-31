from __future__ import annotations
from yogi import read, tokens

class DisjointSet:
    parent: dict[int, int]
    friends: dict[int, int]
    
    def __init__(self) -> None:
        self.parent = {}
        self.friends = {}

    def makeset(self, x: int) -> None:
        self.parent[x] = x
        self.friends[x] = 1

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        prnt_x = self.find(x)
        prnt_y = self.find(y)
        if prnt_x == prnt_y:
            return None
        
        # Assegurar-se de que x sigui el que més amics té (per mantenir el conjunt balancejat)
        if self.friends[prnt_x] < self.friends[prnt_y]:
            prnt_x, prnt_y = prnt_y, prnt_x

        self.parent[prnt_y] = prnt_x
        self.friends[prnt_x] += self.friends[prnt_y]
    
    def num_friends(self, x: int) -> int:
        return self.friends[self.find(x)]


def main() -> None:
    for n in tokens(int):
        q = read(int)

        set_friends = DisjointSet()
        for i in range(1, n + 1):
            set_friends.makeset(i)

        for _ in range(q):
            op = read(str)

            if op == "a":
                x, y = read(int), read(int)
                set_friends.union(x, y)

            elif op == "c":
                x = read(int)
                print(set_friends.num_friends(x))

            else:
                raise KeyError
            
        print("-" * 10)

if __name__ == "__main__":
    main()
