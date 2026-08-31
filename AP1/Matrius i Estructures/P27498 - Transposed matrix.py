def transpose(m: list[list[int]]) -> None:
    n = len(m)
    m[:] = [[m[i][j] for i in range(n)] for j in range (n)]