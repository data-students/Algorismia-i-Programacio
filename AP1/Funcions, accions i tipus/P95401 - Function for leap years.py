def is_leap_year(year: int) -> bool:
    if year % 100 == 0:
        if (year // 100) % 4 == 0:
            return True
        else:
            return False
    
    if year % 4 == 0:
        return True
    
    return False