import heapq
from yogi import tokens, read

Weight = int
Node = int
Arc = tuple[Weight, Node]
ListAdj = list[Arc]
Graph = list[ListAdj]

def cal_sum_mst(G: Graph) -> int:
    """Retorna la suma total dels pesos del mst d'un graf G donat."""

    v = len(G)
    visited = [False] * v
    pq: list[Arc] = []
    
    visited[0] = True
    pq = G[0][:]
    heapq.heapify(pq)
    
    sum_weight = 0
    total_v = 1
    # Aplicar algorisme de Prim
    while total_v < v:  
        weight_curr_arc, curr_arc = heapq.heappop(pq)
        if not visited[curr_arc]:
            visited[curr_arc] = True
            total_v += 1
            sum_weight += weight_curr_arc
            for adj_arc in G[curr_arc]:
                heapq.heappush(pq, adj_arc)
    
    return sum_weight

def main() -> None:
    """Programa principal"""
    for n in tokens(int):
        m = read(int)
        G: Graph = [[] for _ in range(n)]

        for _ in range(m):
            u, v, w = read(int) - 1, read(int) - 1, read(int)
            G[u].append((w, v))
            G[v].append((w, u))
        
        print(cal_sum_mst(G))

if __name__ == "__main__":
    main()