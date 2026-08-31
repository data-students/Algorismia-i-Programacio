from yogi import read, tokens

def max_prize_rec(m: int, M: list[list[int]], sol: list[int], visited: list[bool], idx: int, curr_prize: int, curr_prefix: int) -> int:
    n = len(M)
    if idx == n:
        return curr_prize
    
    max_prize = 0
    for num in range(n):
        if not visited[num]:
            # Descartar num si el prefix es multiple de m
            prefix = (curr_prefix * 10) + num + 1
            if prefix % m == 0:
                continue

            sol[idx] = num
            visited[num] = True

            add_prize = 0
            if idx - 1 >= 0:
                add_prize = M[sol[idx - 1]][sol[idx]]

            find_prize = max_prize_rec(m, M, sol, visited, idx + 1, curr_prize + add_prize, prefix)

            # Actualitzar valor màxim si en trobem un de millor
            if find_prize > max_prize:
                max_prize = find_prize
            
            sol[idx] = -1
            visited[num] = False

    return max_prize

def max_prize(m: int, M: list[list[int]]) -> int:
    n = len(M)
    sol = [-1] * n
    visited = [False] * n

    return max_prize_rec(m,  M, sol, visited, 0, 0, 0)

def main() -> None:
    for m in tokens(int):
        n = read(int)
        M = [[read(int) for _ in range(n)] for _ in range(n)]
        print(max_prize(m, M))

if __name__ == "__main__":
    main()