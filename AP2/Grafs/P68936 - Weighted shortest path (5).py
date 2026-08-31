from yogi import tokens, read
from typing import Optional

Node = int
Weight = int
Arc = tuple[Weight, Node]
ListAdj = list[Arc]
DirGraph = list[ListAdj]

def backtracking(list_prev: list[Node], ini: int, end: int) -> list[Node]:

    trace: list[Node] = []
    prev_node = end
    trace.append(end)
    while prev_node != ini:
        prev_node = list_prev[prev_node]
        trace.append(prev_node)
    trace.reverse
    return trace

def coche_ford(G: DirGraph, ini: int, end: int) -> Optional[int]:
    n = len(G)
    distances = [float("inf")] * n
    distances[ini] = 0

    prev: list[Node] = [-1 for _ in range(n)]
    
    for _ in range(n):
        for curr_node in range(n):
            for adj_node, weight_adj_node in G[curr_node]:
                if distances[adj_node] > distances[curr_node] + weight_adj_node:
                    distances[adj_node] = distances[curr_node] + weight_adj_node
                    prev[adj_node] = curr_node

    return int(distances[end]) if distances[end] != float("inf") else None

def main() -> None:
    for n in tokens(int):
        m = read(int)
        G: DirGraph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, c = read(int), read(int), read(int)
            G[u].append((v, c))
        
        x, y = read(int), read(int)

        shortest_distance = coche_ford(G, x, y)

        print(shortest_distance) if shortest_distance is not None else print(f'no path from {x} to {y}')

if __name__ == "__main__":
    main()