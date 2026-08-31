'''
# Version 1
def number_of_digits (n: int) -> int:
    digits = 0
    if n == 0:
        digits = 1

    while n > 0:
        digits += 1
        n -= n % 10**digits

    return digits
'''

# Version 2
def number_of_digits(n: int) -> int:
    return len(str(n))