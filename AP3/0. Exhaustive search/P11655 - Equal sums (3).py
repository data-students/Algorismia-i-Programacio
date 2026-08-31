from yogi import read


def write_subsets_rec(x: list[int], s: int, sol: list[bool], idx: int, curr_sum: int, rest_sum: int) -> None:

    if curr_sum > s or curr_sum + rest_sum < s:
        return
    
    n = len(x)
    if idx == n:
        if curr_sum== s:
            tmp = [str(x[i]) for i in range(n) if sol[i]]
            print("{" + ",".join(tmp) + "}")
    else:
        sol[idx] = True
        write_subsets_rec(x, s, sol, idx + 1, curr_sum+x[idx], rest_sum - x[idx])
        
        sol[idx] = False
        write_subsets_rec(x, s, sol, idx + 1, curr_sum, rest_sum - x[idx])

def write_subsets(x: list[int], s: int) -> None:
    n = len(x)
    sol = [False] * n
    idx = 0
    curr_sum = 0
    rest_sum = sum(x)
    write_subsets_rec(x, s, sol, idx, curr_sum, rest_sum)

def main() -> None:
    s, n, = read(int), read(int)
    x = [read(int) for _ in range(n)]
    write_subsets(x, s)

if __name__ == "__main__":
    main()