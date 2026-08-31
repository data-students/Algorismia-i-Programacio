import yogi
from typing import TypeAlias

Node: TypeAlias = int
LlistaAdj: TypeAlias = list[Node]
Graf: TypeAlias = list[LlistaAdj]

def dfs(G: Graf, u: Node, visitats: list[bool]) -> None:
    if not visitats[u]:
        visitats[u] = True
        for v in G[u]:
            dfs(G, v, visitats)

def connectats(G: Graf, ori: Node, dst: Node) -> bool:
    n = len(G)
    visitats = [False for _ in range(n)]
    dfs(G, ori, visitats)
    return visitats[dst]


def main() -> None:
    n = yogi.read(int)
    index: dict[str, int] = {}
    for i in range(n):
        index[yogi.read(str)] = i
    m = yogi.read(int)
    G: Graf = [[] for _ in range(n)]
    for _ in range(m):
        u, v = yogi.read(str), yogi.read(str)
        G[index[u]].append(index[v])
    ori, dst = yogi.read(str), yogi.read(str)
    if connectats(G, index[ori], index[dst]):
        print("yes")
    else:
        print("no")


main()
