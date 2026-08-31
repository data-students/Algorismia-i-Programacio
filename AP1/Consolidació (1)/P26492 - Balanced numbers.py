def is_balanced(n: int) -> bool:
    sum_odd = 0
    sum_even = 0

    is_odd_position = False

    while n != 0:
        if is_odd_position:
            sum_odd += n % 10
            is_odd_position = False
        else:
            sum_even += n % 10
            is_odd_position = True
        
        n = n // 10
    
    return sum_odd == sum_even