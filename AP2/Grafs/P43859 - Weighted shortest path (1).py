from yogi import tokens, read
import heapq
from typing import Optional

Node = int
Weight = int
Arc = tuple[Weight, Node]
ListAdj = list[Arc]
DirGraph = list[ListAdj]

def dijkstra(G: DirGraph, ini: int, end: int) -> Optional[int]:
    n = len(G)
    distances = [float("inf")] * n
    distances[ini] = 0
    pq = [(0, ini)]  # (dist, node)

    while pq:
        dist, curr_node = heapq.heappop(pq)
        
        if curr_node == end:
            return dist
        
        if dist > distances[curr_node]:
            continue
        
        for adj_node, weight in G[curr_node]:
            new_dist = dist + weight
            if new_dist < distances[adj_node]:
                distances[adj_node] = new_dist
                heapq.heappush(pq, (new_dist, adj_node))

    return int(distances[end]) if distances[end] != float("inf") else None

def main() -> None:
    for n in tokens(int):
        m = read(int)
        G: DirGraph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, c = read(int), read(int), read(int)
            G[u].append((v, c))
        
        x, y = read(int), read(int)
        
        shortest_path = dijkstra(G, x, y)

        print(shortest_path) if shortest_path is not None else print(f'no path from {x} to {y}')

if __name__ == "__main__":
    main()
