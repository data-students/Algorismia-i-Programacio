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


def llegir_graf() -> Graf:
    n, m = yogi.read(int), yogi.read(int)
    G: Graf = [[] for _ in range(n)]
    for _ in range(m):
        u, v = yogi.read(int), yogi.read(int)
        G[u].append(v)
    return G


def main() -> None:
    G = llegir_graf()
    ori, dst = yogi.read(int), yogi.read(int)
    if connectats(G, ori, dst):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
