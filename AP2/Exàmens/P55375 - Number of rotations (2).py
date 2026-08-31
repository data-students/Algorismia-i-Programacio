def number_of_rotations(v: list[int]) -> int:
    return recursion(v, 0, len(v) - 1)

def recursion (v: list[int], l: int, h: int) -> int:

    if l >= h:
        return l
    else:
        mid = (l + h) // 2
        if v[mid] < v[h]:
            return recursion(v, l, mid)
        else:
            return recursion(v, mid + 1, h)