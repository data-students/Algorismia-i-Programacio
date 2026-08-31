from yogi import tokens

def write_sums(M: list[list[int]]) -> None:
    r, c = len(M), len(M[0])
    S = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            S[i][j] = M[i][j]
            if i > 0:
                S[i][j] += S[i - 1][j]
            if j > 0:
                S[i][j] += S[i][j - 1]
            if i > 0 and j > 0:
                S[i][j] -= S[i - 1][j - 1]
    for row in S:
        print(" ".join(str(x) for x in row))

def char_to_num(c: str) -> int:
    assert len(c) == 1
    n = ord(c) - ord("A") + 1
    return n*(n+1)//2

def main() -> None:
    M = list[list[int]]()
    for row in tokens(str):
        M.append([char_to_num(x) for x in row])
    write_sums(M)


if __name__ == "__main__":
    main()