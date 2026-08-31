from yogi import read, tokens

UNDEF = -1
           
def cn_rec(G: list[list[int]], max_colors: int, colors: list[int], curr_node: int) -> bool:
    
    n = len(G)

    # Cas base
    if curr_node == n:
        return True

    # Cas recursiu
    for k in range(max_colors):
        if all(colors[v] != k for v in G[curr_node]):
            colors[curr_node] = k
            if cn_rec(G, max_colors, colors, curr_node + 1):
                return True
            colors[curr_node] = UNDEF
    return False

def chromatic_number(G: list[list[int]]) -> int:
    n = len(G)
    min_colors = 1
    while True:
        if cn_rec(G, min_colors, [UNDEF] * n, 0):
            break
        min_colors += 1
    
    return min_colors

def main() -> None:
    for n in tokens(int):
        m = read(int)
        G: list[list[int]] = [[] for _ in range(n)]
        for _ in range(m):
            u, v = read(int), read(int)
            G[u].append(v)
            G[v].append(u)
        
        print(chromatic_number(G))


if __name__ == "__main__":
    main()