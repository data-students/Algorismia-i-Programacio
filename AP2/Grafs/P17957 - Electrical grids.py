from collections import deque
from yogi import read, tokens

Node = int
ListAdj = list[Node]
Graph = list[ListAdj]
Flow = list[dict[Node,int]]


def min_flow_in_path(G: Graph, prev: list[int], f: Flow) -> int:
    """Troba un camí entre s i t aplicant bfs i retorna el flow minim que
    pot passar en aquest. Si no hi ha camí, retorna 0. A més modifica la lista
    prev que indica aques camí."""
    s = 0
    t = len(G) - 1
    
    for i in range(len(prev)):
        prev[i] = -1

    mf = float("inf")
    dq: deque[tuple[Node, float]] = deque()
    dq.append((s, mf))

    while dq:
        u, uf = dq.popleft()
        for v in G[u]:
            # Si encara pot haver flow, no l'hem visitat i no és el source
            if f[u][v] > 0 and prev[v] == -1 and v != s:
                prev[v] = u
                mf = min(uf, float(f[u][v]))
                if v == t:
                    return int(mf)
                dq.append((v, mf))
    return 0

def update_edges(f: Flow, prev: list[int], mf: int):
    """Actualitza el flow del graf restant mf al camí de prev"""
    s = 0
    t = len(prev) - 1
    u = t
    while u != s:
        v = prev[u]
        f[v][u] -= mf
        f[u][v] += mf
        u = v

def coche_ford(G: Graph, f: Flow) -> int:
    maxflow = 0
    n = len(G)
    prev = [-1] * n
    mf = min_flow_in_path(G, prev, f)
    while mf > 0:
        maxflow += mf
        update_edges(f, prev, mf)
        mf = min_flow_in_path(G, prev, f)
    return maxflow

def read_graph(n: int, m: int) -> tuple[Graph, Flow]:
    """..."""
    g: Graph = [[] for _ in range(n)]
    f: Flow = [{} for _ in range(n)]

    for _ in range(m):
        u, v, w = read(int), read(int), read(int)
        if v not in g[u]:
            g[u].append(v)
        if u not in g[v]:
            g[v].append(u)

        if v in f[u]:
            f[u][v] += w
        else:
            f[u][v] = w

        if u not in f[v]:
            f[v][u] = 0

    return g, f

def main() -> None:
    for n in tokens(int):
        m = read(int)
        g, f = read_graph(n, m)
        print(ford_fulkerson(g, f))

if __name__ == "__main__":
    main()
