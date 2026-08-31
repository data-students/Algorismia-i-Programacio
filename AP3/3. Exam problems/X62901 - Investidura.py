from yogi import read

def escriu_investidures(a_favor: list[int], en_contra: list[int], abstencio: list[int], president: list[int]) -> None:
    print("President de", end="")
    for i in president:
        print(f" {i}", end="")
    print()

    print("A favor", end="")
    for i in a_favor:
        print(f" {i}", end="")
    print()

    print("Abstencio", end="")
    for i in abstencio:
        print(f" {i}", end="")
    print()

    print("En contra", end="")
    for i in en_contra:
        print(f" {i}", end="")
    print()
    print()

def investidures_rec(
        e: list[int], p: list[int], m: int, idx: int, usats: list[bool],
        a_favor: list[int], abstencio: list[int], en_contra: list[int],
        esc_a_favor: int, esc_en_contra: int, esc_restants: int,
        perfil_min: int, perfil_max: int,
        ) -> None:

    # Poda
    if esc_a_favor + esc_restants <= esc_en_contra:
        return
    
    n = len(e)

    # Cas Base
    if idx == n:
        if esc_a_favor > esc_en_contra:
            max_escaons = max(e[i] for i in a_favor)
            president = [i for i in a_favor if e[i] == max_escaons]
            escriu_investidures(a_favor, en_contra, abstencio, president)
        return
    
    # Cas recursiu

    # En contra
    en_contra.append(idx)
    investidures_rec(e, p, m, idx+1, usats,
                        a_favor, abstencio, en_contra,
                        esc_a_favor, esc_en_contra+e[idx], esc_restants-e[idx],
                        perfil_min, perfil_max)
    en_contra.pop()

    if perfil_min == -1:
        perfil_min = perfil_max = p[idx]

    perfil_min = min(perfil_min, p[idx])
    perfil_max = max(perfil_max, p[idx])

    if perfil_max - perfil_min <= m:
        # Abstenció
        abstencio.append(idx)
        investidures_rec(
            e, p, m, idx+1, usats,
            a_favor, abstencio, en_contra,
            esc_a_favor, esc_en_contra, esc_restants-e[idx],
            perfil_min, perfil_max
        )
        abstencio.pop()

        # A favor
        a_favor.append(idx)
        investidures_rec(
            e, p, m, idx+1, usats,
            a_favor, abstencio, en_contra,
            esc_a_favor+e[idx], esc_en_contra, esc_restants-e[idx],
            perfil_min, perfil_max
        )
        a_favor.pop()



def investidures(e: list[int], p: list[int], m: int) -> None:
    a_favor = list[int]()
    abstencio = list[int]()
    en_contra = list[int]()
    usats = [False] * len(e)
    esc_totals = sum(e)

    investidures_rec(e, p, m, 0, usats, a_favor, abstencio, en_contra, 0, 0, esc_totals, -1, -1)

def main() -> None:
    n = read(int)
    e = list[int]()
    p = list[int]()
    for _ in range(n):
        e.append(read(int))
        p.append(read(int))
    
    m = read(int)

    investidures(e, p, m)
        
if __name__ == "__main__":
    main()