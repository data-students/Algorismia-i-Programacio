import yogi

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

def quick_sort(a: list[int], left: int = 0, right: int = -1) -> None:
    """sorts a[left..right].
    If right < 0, it sorts the whole list.
    The initial call can be invoked as quick_sort(a)
    """
    if right < 0: # initial call (sort the whole list)
        right = len(a)-1
    if left < right:
        mid = partition(a, left, right)
        quick_sort(a, left, mid)
        quick_sort(a, mid+1, right)

def msort(lst: list[int]) -> list[int]:
    cpy = lst[:]
    quick_sort(cpy)
    return cpy


def main() -> None:

    lst = [entrada for entrada in yogi.tokens(int)]
    lst = msort(lst)
    for num in lst:
        print(num)

if __name__ == "__main__":
    main()