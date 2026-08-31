"""
Idea: calcular las combinaciones a partir de dos posibilidades:
    (expresion) = correct_expressions[n - 2]
    (expresion) - (expresion) = suma (c_e [n - 5 - i] * c_e [n - 5 - i']) donde n - 5 - i + n - i' = n -> n - 5 - i - i ' = 0 -> i' = n - 5 - i
    """

from yogi import read, tokens

def correct_expressions_rec(n: int, m: int, cache: list[int]) -> int:
    if n <= 0:
        return 0
    
    if cache[n] != -1:
        return cache[n]
    
    if n == 1:
        return m
    
    par = correct_expressions_rec(n - 2, m, cache)
    rest = 0
    for i in range(1, n - 5):
        rest += correct_expressions_rec(n - 5 - i, m, cache) * correct_expressions_rec(i, m, cache)
    ret = par + rest
    cache[n] = ret
    return ret

def correct_expressions(n: int, m: int) -> int:
    cache = [-1] * (n + 1)
    return correct_expressions_rec(n, m, cache)

def main() -> None:
    for n in tokens(int):
        m = read(int)
        print(correct_expressions(n, m))

if __name__ == "__main__":
    main()