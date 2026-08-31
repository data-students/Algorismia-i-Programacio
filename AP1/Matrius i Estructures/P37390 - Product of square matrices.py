from typing import TypeAlias

Matrix: TypeAlias = list[list[int]]
def product(a: Matrix, b: Matrix) -> Matrix:
    '''Donades dues matrius a i b, retorna la multiplicacio de les dues matrius'''
    return [[sum([a[i][k] * b[k][j] for k in range(len(b))]) for j in range (len(b[0]))] for i in range(len(a))]