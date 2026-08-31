from yogi import read, tokens
import heapq

Node = int
Cost = int
Evaporation = int
Arc = tuple[Evaporation, Cost, Node]
ListAdj = list[Arc]
Graph = list[ListAdj]

def minimize(G: Graph) -> tuple[int, int]:
    
    n = len(G)
    visited = [False] * n
    min_ev = min_cost = 0

    pq: list[Arc] = [(0, 0, 0)] # cua de prioritat (ev, cost, node) inicialitzada pel node 0
    heapq.heapify(pq)
    i = 0

    while i < n:
        curr_ev, curr_c, curr_node = heapq.heappop(pq)
        if not visited[curr_node]:
            visited[curr_node] = True
            min_ev += curr_ev
            min_cost += curr_c
            i += 1
            for adj_node in G[curr_node]:
                if not visited[adj_node[2]]:
                    heapq.heappush(pq, adj_node)

    return min_ev, min_cost



def main() -> None:
    for n in tokens(int):
        m = read(int)
        G: Graph = [[] for _ in range(n)]
        for _ in range(m):
            x, y, v, c = read(int), read(int), read(int), read(int)
            G[x].append((v, c, y))
            G[y].append((v, c, x))
        
        print(*minimize(G))


if __name__ == "__main__":
    main()