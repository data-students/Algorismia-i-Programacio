def is_symmetric(m: list[list[int]]) -> bool:
    llargada = len(m)
    for i in range (llargada):
        for j in range (i):
            if m[i][j] != m [j][i]:
                return False
    else:
        return True




'''
matriu: list[list[int]] = [
    [5, 7, 6, 4, 1, 2],
    [2, 8, 1, 3, 8, 8],
    [0, 1, 2, 9, 2, 1],
    [6, 5, 4, 3, 2, 1],
    [0, 1, 2, 9, 2, 1]
]
print (matriu)
is_symmetric(matriu)
print (matriu)
'''
