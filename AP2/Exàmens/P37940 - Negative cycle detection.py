from yogi import read, tokens

Node = int
Weight = int
Arc = tuple[Node, Weight]
ListAdj = dict[Node, Weight]
Graph = list[ListAdj]

def is_cyclic(G: Graph) -> bool:
    """Donat un graf G, retorna 'True' si G conté un cicle dins, retorna 'False' alternament."""
    n = len(G)
    dists = [-1] * n
    dists[0] = 0

    # Aplicar l'algorisme de Bellman-Ford (N-1) vegades
    for _ in range(n):
        for u in range(n):
            for v in G[u]:
                if dists[v] > dists[u] + G[u][v]:
                    dists[v] = dists[u] + G[u][v]
    
    # Si apliquem l'algorisme una iteració més i alguna de 
    # les distàncies ha decrescut, hi ha un cicle.
    dists_cycle = dists.copy()
    for u in range(n):
        for v in G[u]:
            if dists_cycle[v] > dists_cycle[u] + G[u][v]:
                dists_cycle[v] = dists_cycle[u] + G[u][v]
    
    for i in range(n):
        if dists_cycle[i] < dists[i]:
            return True

    return False

def main() -> None:
    """Programa principal."""
    for n in tokens(int):
        m = read(int)
        G: Graph = [{} for _ in range(n)]
        for _ in range(m):
            u, v, w = read(int), read(int), read(int)
            G[u][v] = w
        print("YES" if is_cyclic(G) else "NO")

if __name__ == "__main__":
    main()