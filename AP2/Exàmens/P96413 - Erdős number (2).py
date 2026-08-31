from yogi import tokens, read
from collections import deque

Node = int
listAdj = set[Node]
Graph = list[listAdj]

def calc_erdos_number(G: Graph) -> dict[int, int]:
    """..."""
    n = len(G)
    dists = {i: -1 for i in range(n)} # the distance from 0 is the erdos_number
    dists[0] = 0
    # Do a BFS
    dq = deque([0])
    while dq:
        curr_node = dq.popleft()
        for adj_node in G[curr_node]:
            if dists[adj_node] == -1:
                dists[adj_node] = dists[curr_node] + 1
                dq.append(adj_node)
    return dists

def read_works(n: int, w: int) -> Graph:
    """..."""
    G: Graph = [set() for _ in range(n)]
    for _ in range(w):
        i = read(int)
        coautors = [read(int) for _ in range(i)]
        for u in coautors:
            for v in coautors:
                if u != v:
                    G[u].add(v)
                    G[v].add(u)
    return G

def main() -> None:
    for n in tokens(int):
        w = read(int)
        G = read_works(n, w)
        dists = calc_erdos_number(G)
        for person, erdos in dists.items():
            print(person, ": ", end="")
            print(erdos) if erdos != -1 else print("no")
        print("-" * 10)

if __name__ == "__main__":
    main()