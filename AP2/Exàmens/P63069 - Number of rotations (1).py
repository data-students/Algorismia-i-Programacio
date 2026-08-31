def number_of_rotations(v: list[int]) -> int:
    '''Given a (non empty) circularly sorted vector of integers, 
    returns the number of times the vector is rotated.'''
    left = 0
    right = len(v) - 1
        
    while left < right:
        mid = (left + right) // 2

        if v[mid] < v[right]:
            right = mid
        else: 
            left = mid + 1   
    
    return right