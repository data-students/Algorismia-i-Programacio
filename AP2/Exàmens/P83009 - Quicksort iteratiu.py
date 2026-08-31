import fileinput


def quicksort(array: list[str]) -> None:
    quicksort_iter(array, 0, len(array) - 1)

def quicksort_iter(array: list[str], left: int, right: int) -> None:

    pila: list[tuple[int, int]] = [(left, right)]
    while pila:
        current = pila.pop()
        l, r = current
        if l < r:
            mid = partition(array, l, r)
            pila.append((l, mid))
            pila.append((mid + 1, r))

def partition(array: list[str], left: int, right: int) -> int:
    pivot = array[left]
    i, j = left - 1, right + 1
    while True:
        while True:
            i += 1
            if array[i] >= pivot: break
        while True:
            j -= 1
            if array[j] <= pivot: break
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def main() -> None:
    for line in fileinput.input():
        array = line.strip().split()
        quicksort(array)
        print(*array)


if __name__ == "__main__":
    main()
