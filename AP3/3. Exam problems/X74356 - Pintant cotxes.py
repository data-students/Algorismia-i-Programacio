import sys
from yogi import tokens, read

recursions = 0

def min_cost_rec(
        cost_nateja: list[list[int]], color: list[int], cost: int, sol: list[int],
        millor_cost: int, millor_sol: list[int], usats: list[bool]
                 ) -> tuple[list[int], int]:
    global recursions
    recursions += 1

    # Poda
    if cost > millor_cost:
        return millor_sol, millor_cost
    
    idx = len(sol)
    n = len(cost_nateja)
    m = len(color)

    # Cas base
    if idx == m:
        if cost < millor_cost:
            millor_sol, millor_cost = sol[:], cost
        return millor_sol, millor_cost
    
    # Cas recursiu
    for k in range(m):
        if usats[k]:
            continue
        color_ant = color[sol[-1]] if sol else color[k]
        usats[k] = True
        sol.append(k)

        millor_sol, millor_cost = min_cost_rec(cost_nateja, color, cost + cost_nateja[color_ant][color[k]], sol, millor_cost, millor_sol, usats)

        usats[k] = False
        sol.pop()
    
    return millor_sol, millor_cost

def min_cost(cost_nateja: list[list[int]], color: list[int]) -> tuple[list[int], int]:

    m = len(color)
    usats = [False] * m

    return min_cost_rec(cost_nateja, color, 0, [], sys.maxsize, [], usats)


def main() -> None:
    global recursions
    for n in tokens(int):
        cost_nateja = [[read(int) for _ in range(n)] for _ in range(n)]
        m = read(int)
        color = [read(int) for _ in range(m)]

        print(min_cost(cost_nateja, color))

        print(recursions)
        print()

if __name__ == "__main__":
    main()