from yogi import read, tokens
import heapq

Node = int
Weight = int
ListAdj = list[tuple[Weight, Node]]
Graph = list[ListAdj]

def bfs(G: Graph, hotel: list[int], a: int, b: int) -> int:
    n = len(G)

    dists = [-1] * n
    dists[a] = 0
    pq = [(0, a)]

    while pq:
        curr_weight, curr_node = heapq.heappop(pq)

        if curr_node == b:
            return curr_weight
        
        for adj_weight, adj_node in G[curr_node]:
            new_adj_dist = dists[curr_node] + adj_weight + (0 if adj_node == b else hotel[adj_node])
            if new_adj_dist < dists[adj_node] or dists[adj_node] == -1:
                dists[adj_node] = new_adj_dist
                heapq.heappush(pq, (new_adj_dist, adj_node))

    return -1

def read_graph() -> tuple[Graph, list[int]]:

    n, m = read(int), read(int)

    hotel = [read(int) for _ in range(n)]

    G: Graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = read(int), read(int), read(int)
        G[u].append((w, v))
        G[v].append((w, u))

    return G, hotel

def main() -> None:
    G, hotel = read_graph()
    for a in tokens(int):
        b = read(int)
        if a != b:
            dist = bfs(G, hotel, a, b)
        else:
            dist = 0
        print(f"c({a},{b}) = ", end="")
        print(dist) if dist != -1 else print("+oo")

if __name__ == "__main__":
    main()
