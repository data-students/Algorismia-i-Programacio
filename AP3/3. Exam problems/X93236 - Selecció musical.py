from yogi import read

def esm_rec(idx: int, k: int, sol: list[int],
            cancons_per_amic: list[list[bool]], rem_cancons: list[int],
            cancons_sat: list[int], amics_sat: int
            ) -> None:
    
    n = len(cancons_per_amic[0])
    m = len(cancons_per_amic)

    # Cas base
    if idx == n or len(sol) > k:
        if amics_sat == m and len(sol) <= k:
            print(",".join(str(x) for x in sol))
        return

    # Poda un amic insatisfet ja no té cancons que el puguin satisfer
    for amic in range(m):
        if cancons_sat[amic] == 0 and rem_cancons[amic] == 0:
            return
        
    # Cas recursiu
    for amic in range(m):
        if cancons_per_amic[amic][idx]:
            rem_cancons[amic] -= 1

    # No posar la canco
    esm_rec(idx + 1, k, sol, cancons_per_amic, rem_cancons, cancons_sat, amics_sat)
    
    # Posar la canco
    sol.append(idx)
    for amic in range(m):
        if cancons_per_amic[amic][idx]:
            cancons_sat[amic] += 1
            if cancons_sat[amic] == 1:
                amics_sat += 1

    esm_rec(idx + 1, k, sol, cancons_per_amic, rem_cancons, cancons_sat, amics_sat)

    sol.pop()
    for amic in range(m):
        if cancons_per_amic[amic][idx]:
            cancons_sat[amic] -= 1
            if cancons_sat[amic] == 0:
                amics_sat -= 1
    
    for amic in range(m):
        if cancons_per_amic[amic][idx]:
            rem_cancons[amic] += 1


def escriu_seleccions_musicals(n: int, m: int, cancons_per_amic: list[list[bool]], k: int) -> None:
    rem_cancons = [sum(cancons_per_amic[amic][canco] for canco in range(n)) for amic in range(m)] # Nombre potencial d'amics que pot satisfer la canco i
    cancons_sat = [0] * m # Nombre de cancons que satisfan a l'amic i

    esm_rec(0, k, [], cancons_per_amic, rem_cancons, cancons_sat, 0)

def main() -> None:
    n = read(int) # nombre de cancons
    m = read(int) # nombre de amics
    cancons_per_amic = [[False] * n for _ in range(m)] # list[amic][canco] 
    for amic in range(m):
        for _ in range(read(int)):
            cancons_per_amic[amic][read(int)] = True
    k = read(int)

    escriu_seleccions_musicals(n, m, cancons_per_amic, k)

if __name__ == "__main__":
    main()
