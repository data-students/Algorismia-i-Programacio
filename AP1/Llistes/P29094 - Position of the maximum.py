def position_maximum(v: list[float], m: int) -> int:
    '''
    Returns the position of the maximum element of v[0..m]. If there is a tie, the smaller position must be returned.
    Prec: 0 ≤ m < size of v.
'''
    max_position = 0
    max_number = v[0]

    i = 0
    while i <= m:
        current_number = v[i]
        if current_number > max_number:
            max_number = current_number
            max_position = i
        else:
            i += 1
    
    return max_position
