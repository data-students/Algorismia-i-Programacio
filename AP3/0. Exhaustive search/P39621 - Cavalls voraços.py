from yogi import read, tokens

def atacada(sol: list[list[bool]], i: int, j: int) -> bool:
    n, m = len(sol), len(sol[0])
    dirs = [(-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    for di, dj in dirs:
        new_i = i + di
        new_j = j + dj
        if 0 <= new_i < n and 0 <= new_j < m and sol[new_i][new_j]:
            return True
    return False

def max_monedes_rec(M: list[list[int]], sol: list[list[bool]], i: int, j: int, monedes_actuals: int) -> int:
    
    n, m = len(M), len(M[0])
    if j == m:
        return max_monedes_rec(M, sol, i + 1, 0, monedes_actuals)

    if i == n:
        return monedes_actuals

    else:
        sol[i][j] = False # No poso cavall
        m1 = max_monedes_rec(M, sol, i, j + 1, monedes_actuals)

        m2 = 0
        if not atacada(sol, i, j):
            sol[i][j] = True # Poso cavall
            m2 = max_monedes_rec(M, sol, i, j + 1, monedes_actuals + M[i][j])
        
        return max(m1, m2)


def max_monedes(M: list[list[int]]) -> int:
    n, m = len(M), len(M[0])
    sol = [[False] * m for _ in range(n)]
    i = j = monedes_actuals = 0

    return max_monedes_rec(M, sol, i, j, monedes_actuals)

def main() -> None:
    for n in tokens(int):
        m = read(int)
        M = [[read(int) for _ in range(m)] for _ in range(n)]
        print(max_monedes(M))

if __name__ == "__main__":
    main()
