def position(x: float, v: list[float], left: int, right: int) -> int:
    if left > right or left < 0 or right >= len(v):
        return -1
    
    while left <= right:
        mid = (left + right) // 2
        if v[mid] > x:
            right = mid - 1
        elif v[mid] < x:
            left = mid + 1
        else:
            return mid
    
    return -1