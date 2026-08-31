from yogi import read, tokens
from collections import deque
Node = int
ListAdj = list[Node]
Graph = list[ListAdj]

def has_cycle(g: Graph) -> bool:
    """Utilitza dfs per saber si hi han cicles en un graf. Si es
    dona el cas, retorna 'True'. Retorna 'False' alternament."""
    n = len(g)

    visited = [False] * n
    in_queue = [False] * n
    dq: deque[int] = deque([0])
    while dq:
        curr_node = dq.pop()
        in_queue[curr_node] = False
        for adj_node in g[curr_node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                if in_queue[adj_node]:
                    return True
                dq.append(adj_node)
                in_queue[adj_node] = True

    return False

def read_graph(n: int, m: int) -> Graph:
    g: Graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = read(int), read(int)
        g[u].append(v)
    
    return g
    
def main() -> None:
    for n in tokens(int):
        m = read(int)
        g = read_graph(n, m)
        print("yes") if has_cycle(g) else print("no")


if __name__ == "__main__":
    main()