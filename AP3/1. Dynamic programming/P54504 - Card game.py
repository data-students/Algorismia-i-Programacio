from yogi import read
from sys import maxsize

UNDEF = -1
INF = 500_000

def min_cards(n: int, cache: list[int]) -> int:
    if n < 0:
        return maxsize

    if cache[n] != UNDEF:
        return cache[n]
    
    if n == 0:
        return 0

    if n == 1 or n == 5 or n == 8 or n == 14:
        return 1

    find_min = min(min_cards(n - 1, cache), min_cards(n - 5, cache), min_cards(n - 8, cache), min_cards(n - 14, cache)) + 1
    cache[n] = find_min
    return find_min

def main() -> None:
    n = read(int)
    cache = [-1 for _ in range(INF + 1)]
    while n != -1:
        print(min_cards(n, cache))
        n = read(int)

if __name__ == "__main__":
    main()