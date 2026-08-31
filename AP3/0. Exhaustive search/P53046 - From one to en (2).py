from yogi import read

def write_permutations_rec(n: int, poss_num: list[bool], used: list[bool], idx: int, pos: int, sol: list[int]) -> None:
    """..."""
    if idx == n - 1:
        sol[pos] = 0
        print("(" + ",".join([str(x + 1) for x in sol]) + ")")
    else:
        for i in range(n):
            if not used[i] and poss_num[i]:
                sol[pos] = i
                poss_num[pos] = False
                used[i] = True
                write_permutations_rec(n, poss_num, used, idx + 1, i, sol)
                sol[pos] = -1
                poss_num[pos] = True
                used[i] = False

def write_permutations(n: int) -> None:
    """..."""
    sol = [-1] * n
    poss_num = [True] * n
    poss_num[0] = False
    used = [False] * n
    write_permutations_rec(n, poss_num, used, 0, 0, sol)

def main() -> None:
    n = read(int)
    write_permutations(n)

if __name__ == "__main__":
    main()