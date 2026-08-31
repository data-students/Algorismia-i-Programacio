from yogi import read, tokens

Node = int
ListAdj = list[Node]
Graph = list[ListAdj]

def what_color(G: Graph, colors: list[int], u: int, c: int) -> int:
    """Returns the least possible color that u can be colored using at most n.
    Returns -1 if it is not possible."""

    available = [True] * c
    for v in G[u]:
        if colors[v] != -1:
            available[colors[v]] = False

    return available.index(True) if any(available) else -1

def golafre(G: Graph) -> int:
    n = len(G)
    c = 0
    colors = [-1] * n
    for i in range(n):
        color = what_color(G, colors, i, c)
        if color == -1:
            colors[i] = c
            c += 1
        else:
            colors[i] = color
    return c
        

def main() -> None:
    for n in tokens(int):
        m = read(int)
        G: Graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = read(int), read(int)
            G[u].append(v)
            G[v].append(u)
        print(golafre(G))



if __name__ == "__main__":
    main()