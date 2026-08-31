from yogi import read, tokens

UNDEF = -1.0

def td(x: list[float], cache: list[list[float]], i: int, j: int) -> float:

    if cache[i][j] != UNDEF:
        return cache[i][j]

    max_value = UNDEF
    # Cas base:
    if i > j:
        max_value = 0
    elif i == j:
        max_value = x[i] # == return x[j]
    else:
        # Cas recursiu
        for k in range(i, j):
            p_low = td(x, cache, i, k)
            p_top = td(x, cache, k + 1, j)
            max_value = max(p_low + p_top, p_low * p_top, max_value)

    cache[i][j] = max_value
    return max_value


def max_aritmetic_expression(x: list[float]) -> float:
    n = len(x)
    cache = [[UNDEF]* n for _ in range(n)]

    return td(x, cache, 0, n - 1)

def main() -> None:
    for n in tokens(int):
        x = [read(float) for _ in range(n)]
        print(f"{max_aritmetic_expression(x):.04f}")

if __name__ == "__main__":
    main()