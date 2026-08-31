def sum_divisors(x: int) -> int:
    i = 1
    sum = 0

    while i*i <= x:
        if x % i == 0:
            div1 = i
            div2 = x // i
            if div1 == div2:
                sum += div1
            else:
                sum += div1 + div2
        i += 1

    return sum