from yogi import tokens

UNDEF = -1

def paraules(n: int, cache: list[int]) -> int:

    if cache[n] != UNDEF:
        return cache[n]

    if n == 0:
        return 1

    s = 0
    for i in range(2, n+1):
        s += paraules(i-2, cache) * paraules(n-i, cache)
    return s

def main() -> None:
    MAX_NUMBER = 67
    cache = [UNDEF for _ in range(MAX_NUMBER + 1)]
    for n in tokens(int):
        print(paraules(n, cache))


if __name__ == "__main__":
    main()