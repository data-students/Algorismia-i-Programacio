def number_of_digits(n: int) -> int:
    '''Donat un nombre enter, retorna el nombre de digits que té.'''

    return len(str(n))

def is_palindromic(n: int) -> bool:
    '''Donada un nombre enter, retorna "True" si aquest nombre es capicua i retorna "False" en cas contrari.'''

    nStr = str(n) # Transforma el nombre enter en un string
    length = number_of_digits (n)

    for i in range (1, length//2 + 1):

        if nStr [i - 1] != nStr[length - i]: # Si el primer digit és diferent al ultim, si el segon digit és diferent al penúltim...

            return False # ... retorna que NO es capicuca

    return True # ... retorna que SI es capicua
