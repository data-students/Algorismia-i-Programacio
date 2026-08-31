from yogi import read

def max2(a: int, b: int) -> int:
    if a > b:
        return a
    return b

def max4(a: int, b: int, c: int, d: int) -> int:
    return max2(max2(a,b),max2(c,d))