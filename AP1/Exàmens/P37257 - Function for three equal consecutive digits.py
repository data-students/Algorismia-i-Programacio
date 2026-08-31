def three_equal_final_digits (n: int, b: int) -> bool:
    
    d1 = n % b
    d2 = (n // b) % b
    d3 = (n // b * b) % b
    return d1 == d2 == d3

def three_equal_consecutive_digits(n: int, b: int) -> bool:
    if n < b * b:
        return False
    elif three_equal_final_digits(n, b):
        return True
    else:
        return three_equal_consecutive_digits (n // b, b)