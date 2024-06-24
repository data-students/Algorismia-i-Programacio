def sum_of_digits(x: int) -> int:
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


def reduction_of_digits(x: int) -> int:
    if x < 10:
        return x
    else:
        return reduction_of_digits(sum_of_digits(x))
