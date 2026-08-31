from yogi import read, tokens
from typing import Iterator


def collatz(n: int) -> Iterator[int]:
    while n > 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1


def collatz_length(n: int) -> int:
    return len(list(collatz(n)))


def collatz_highest(n: int) -> int:
    highest = 1
    for i in collatz(n):
        highest = max(highest, i)
    return highest


def collatz_highest_position(n: int) -> tuple[int, int]:
    idx = 0
    highest = 1
    for i, val in enumerate(collatz(n)):
        if val > highest:
            highest = val
            idx = i
    return idx, highest


def collatz_11(n: int) -> bool:
    collatz_generator = collatz(n)
    next(collatz_generator)
    return any(i % 11 == 0 for i in collatz_generator)

def collatz_first_common(n1: int, n2: int) -> int:

    c1 = collatz(n1)
    c2 = set(collatz(n2))
    for i in c1:
        if i in c2:
            return i
    return 1


def collatz_common_elements(n1: int, n2: int) -> int:
    com = list(set(collatz(n1)) & set(collatz(n2)))
    return len(com)


def collatz_union(n1: int, n2: int) -> list[int]:
    com = sorted(set(collatz(n1)) | set(collatz(n2)))
    return com

def collatz_top_numbers() -> Iterator[int]:
    abs_max = 0
    n = 1
    while True:
        current_max = collatz_highest(n)
        if current_max > abs_max:
            abs_max = current_max
            yield n
        n += 1


def collatz_first_missing(n: int) -> int:
    
    seq = set(collatz(n))
    candidate = 1
    while True:
        if candidate not in seq:
            return candidate
        candidate += 1


def main() -> None:
    """Main program"""

    for command in tokens(str):
        if command == 'collatz':
            print(*list(collatz(read(int))))
        elif command == 'collatz_length':
            print(collatz_length(read(int)))
        elif command == 'collatz_highest':
            print(collatz_highest(read(int)))
        elif command == 'collatz_highest_position':
            print(collatz_highest_position(read(int)))
        elif command == 'collatz_11':
            print(collatz_11(read(int)))
        elif command == 'collatz_first_common':
            print(collatz_first_common(read(int), read(int)))
        elif command == 'collatz_common_elements':
            print(collatz_common_elements(read(int), read(int)))
        elif command == 'collatz_union':
            print(*collatz_union(read(int), read(int)))
        elif command == 'collatz_top_numbers':
            print(*[v for v, _ in zip(collatz_top_numbers(), range(read(int)))])
        elif command == 'collatz_first_missing':
            print(collatz_first_missing(read(int)))
        else:
            assert False

main()
