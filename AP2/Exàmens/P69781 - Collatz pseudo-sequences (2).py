from yogi import read, tokens
from typing import Iterator

MAX_NUM = 10**8

def collatz_sequence_2(x: int, y: int, n: int) -> Iterator[int]:
    """..."""
    while n <= MAX_NUM:
        yield n
        if n % 2 == 0:
            n = n // 2 + x
        else:
            n = 3 * n + y
    yield n

def main() -> None:
    for x in tokens(int):
        y, n = read(int), read(int)

        set_num: set[int] = set()
        list_num: list[int] = []
        cltz_seq = collatz_sequence_2(x, y, n)
        num = next(cltz_seq)
        try:
            while True:
                if num not in set_num:
                    set_num.add(num)
                    list_num.append(num)
                else:
                    cycle_len = len(list_num) - list_num.index(num)
                    break
                num = next(cltz_seq)

            print(cycle_len)

        except StopIteration:
            print(num)
if __name__ == "__main__":
    main()