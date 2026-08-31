import fileinput


def partition(a: list[int], left: int, right: int) -> int:
    """a[left..right]: segment to be sorted.
    Output: The left part has elements ≤ than the pivot.
    The right part has elements ≥ than the pivot.
    Returns the index of the last element of the left part
    """
    pivot = a[left]
    i, j = left-1, right+1
    while True:
        while True: # find a[i] ≥ pivot
            i += 1
            if a[i] >= pivot: break
        while True: # find a[j] ≤ pivot
            j -= 1
            if a[j] <= pivot: break
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i] # swap a[i], a[j]

def quick_select(a: list[int], k: int, left: int = 0, right: int = -1) -> int:
    """Returns the element at location k assuming
    a[left..right] would be sorted.
    Pre: left ≤ k ≤ right.
    Post: the elements of a have changed their locations.
    The initial call can be invoked as quick_select(a, k)
    """
    if right < 0: # initial call (use the whole list)
        right = len(a)-1
    if left == right:
        return a[left]
    mid = partition(a, left, right)
    if k <= mid:
        return quick_select(a, k, left, mid)
    return quick_select(a, k, mid+1, right)

def median(v: list[int]) -> int:
    mid = len(v) // 2
    return quick_select(v, mid)

def main() -> None:
    for line in fileinput.input():
        print(median([int(x) for x in line.split()]))


if __name__ == '__main__':
    main()
