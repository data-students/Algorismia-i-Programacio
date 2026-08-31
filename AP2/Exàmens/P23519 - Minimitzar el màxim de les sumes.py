import yogi

def has_max_sum(v: list[int], m: int, x: int) -> bool:
    """Indica si es pot tallar v en m trossos de forma que el màxim de les sumes dels trossos sigui x o menys."""
    p_sum = 0
    partitions = 1
    for num in v:
        if num > x:
            return False
        if p_sum + num <= x:
            p_sum += num
        else:
            partitions += 1
            p_sum = num
            if partitions > m:
                return False
            
    return True

def min_max_sum(v: list[int], m: int) -> int:
    """Retorna el mínim dels màxims de les sumes de v en m trossos utilitzant has_max_sum astutament."""
    h = sum(v)
    l = 0
    while h > l:
        mid = (h + l) // 2
        if has_max_sum(v, m, mid):
            h = mid
        else:
            l = mid + 1

    return h

    
def main() -> None:
    for m in yogi.tokens(int):
        n = yogi.read(int)
        v = [yogi.read(int) for _ in range(n)]
        print(min_max_sum(v, m))

if __name__ == "__main__":
    main()