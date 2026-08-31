from yogi import tokens, read
from collections import deque

RED = True
BLUE = False
Color = bool | None # bool: Pintat d'un color, None: no pintat

Node = int
ListAdj = list[Node]
Graph = list[ListAdj]


def is_two_colorable(G: Graph) -> bool:
    n = len(G)
    visited = [False] * n
    colors: list[Color] = [None] * n

    for start_node in range(n):
        if not visited[start_node]:
            dq: deque[int] = deque()
            dq.append(start_node)
            colors[start_node] = RED
            visited[start_node] = True

            while dq:
                curr_node = dq.popleft()
                for adj_node in G[curr_node]:
                    if colors[adj_node] is None:
                        colors[adj_node] = not colors[curr_node]
                        visited[adj_node] = True
                        dq.append(adj_node)
                    elif colors[adj_node] == colors[curr_node]:
                        return False
    return True

def main() -> None:
    for n in tokens(int):
        m = read(int)
        G: Graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = read(int), read(int)
            G[u].append(v)
            G[v].append(u)

        print("yes" if is_two_colorable(G) else "no")

if __name__ == "__main__":
    main()