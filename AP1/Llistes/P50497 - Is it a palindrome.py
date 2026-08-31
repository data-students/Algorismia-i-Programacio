def is_palindrome(s: str) -> bool:
    '''Donat una paraula, retorn "True" si aquesta és palindromica. Retorna "False" alternament.'''
    es_palindromica = True
    llargada = len(s)

    i = 0
    while i < llargada // 2 and es_palindromica:
        if s[i] != s [llargada - i - 1]:
            es_palindromica = False

        i += 1
    
    return es_palindromica