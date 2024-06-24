
def is_increasing(n: int) -> bool:
    if n//10 == 0:
        return True

    return n % 10 >= (n//10) % 10 and is_increasing(n//10)
