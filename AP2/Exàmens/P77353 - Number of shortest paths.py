from yogi import tokens, read
from collections import deque

Node = int
ListAdj = list[Node]
Graph = list[ListAdj]

def number_shortest_path(G: Graph) -> tuple[list[int], list[int]]:
    """..."""
    n = len(G)
    num_shortest_path = [1] * n # number of paths from 0
    dists = [-1] * n # distance from 0, -1 means unreachable
    dists[0] = 0
    dq = deque([0]) # list[tuple[node, num_shortest_paths]]
    while dq:
        curr_node = dq.popleft()
        for adj_node in G[curr_node]:
            # Si es la primera vegada que el visitem
            if dists[adj_node] == -1:
                dists[adj_node] = dists[curr_node] + 1
                num_shortest_path[adj_node] = num_shortest_path[curr_node]
                dq.append(adj_node)

            # Si trobem un camí igual de curt
            elif dists[curr_node] + 1 == dists[adj_node]:
                num_shortest_path[adj_node] += num_shortest_path[curr_node]

            # Obs: per la naturalesa del bfs, com a molt trobarem camins
            # igual de llargs, però no de més curts.

    return dists, num_shortest_path

def main() -> None:
    for n in tokens(int):
        m = read(int)
        G: Graph = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v = read(int), read(int)
            G[u].append(v)

        dists, num_shortest_path = number_shortest_path(G)
        for i in range(n):
            if dists[i] != -1:
                print(f"{i}: {dists[i]} {num_shortest_path[i]}")
            else:
                print(f"{i}: {dists[i]}")
        print()

if __name__ == "__main__":
    main()