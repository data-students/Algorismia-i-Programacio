from yogi import read, tokens
from collections import deque

Node = int
ListAdj = list[Node]
Graph = list[ListAdj]



def get_disatances(G: Graph, usr_to_idx: dict[str, int], s: str, k: int) -> int:

    n = len(G)
    count = 0
    s_idx = usr_to_idx[s]

    dists = [-1] * n
    dists[s_idx] = 0
    dq = deque([s_idx])

    while dq:
        curr_node = dq.popleft()

        if dists[curr_node] > k:
            break

        if dists[curr_node] == k:
            count += 1
        
        for adj_node in G[curr_node]:
            if dists[adj_node] == -1:
                dists[adj_node] = dists[curr_node] + 1
                dq.append(adj_node)

    return count


def main() -> None:

    n, m = read(int), read(int)
    G: Graph = [[] for _ in range(n)]
    usr_to_idx: dict[str, int] = {}
    i = 0

    for i in range(n):
        usr = read(str)
        usr_to_idx[usr] = i

    for _ in range(m):
        u, v = read(str), read(str)
        G[usr_to_idx[u]].append(usr_to_idx[v])
    
    for u in tokens(str):
        k = read(int)
        print(get_disatances(G, usr_to_idx, u, k))
    


if __name__ == "__main__":
    main()