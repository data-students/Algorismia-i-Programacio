def sum(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    llargada = len(a)
    return [[a[i][j] + b[i][j] for j in range (llargada)] for i in range(llargada)]

matriu1: list[list[int]] = [
    [5, 7, 6, 4],
    [2, 8, 1, 3],
    [0, 1, 2, 9],
    [6, 5, 4, 3]
]
matriu2: list[list[int]] = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [9, 8, 7, 6],
    [0, 2, 0, 4]
]
print (sum(matriu1, matriu2))


    