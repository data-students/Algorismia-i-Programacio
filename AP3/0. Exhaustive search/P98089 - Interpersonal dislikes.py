from yogi import read, tokens
from sys import maxsize as giganumero

def min_dislikes_rec(curr_sol: list[int], sol: list[int], dislikes: list[list[int]], 
                     used: list[bool], curr_sum: int, min_sum: int, idx: int) -> tuple[int, list[int]]:
    n = len(dislikes)

    if idx == n:
        return curr_sum, curr_sol[:]
    
    last = curr_sol[-1]

    for i in range(n):
        if not used[i] and curr_sum + dislikes[i][last] < min_sum:
            curr_sol.append(i)
            used[i] = True
            find_sum, find_sol = min_dislikes_rec(curr_sol, sol, dislikes, used, curr_sum + dislikes[i][last], min_sum, idx + 1)
            if find_sum < min_sum:
                min_sum = find_sum
                sol = find_sol
            curr_sol.pop()
            used[i] = False
    return min_sum, sol

def min_dislikes(names: list[str], dislikes: list[list[int]]) -> tuple[int, list[str]]:
    n = len(names)
    idx_to_name = {i: name for i, name in enumerate(names)}
    used = [False]*n
    used[0] = True
    min_sum, sol = min_dislikes_rec([0], [], dislikes, used, 0, giganumero, 1)
    return min_sum, [idx_to_name[i] for i in sol]


def main() -> None:
    for n in tokens(int):
        names = [read(str) for _ in range(n)]

        dislikes = [[read(int) for _ in range(n)] for _ in range(n)]

        min_sum, sol = min_dislikes(names, dislikes)
        print(min_sum)
        print(" ".join(str(x) for x in sol))

if __name__ == "__main__":
    main()