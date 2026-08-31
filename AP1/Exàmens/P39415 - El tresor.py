import yogi

def trobar_tresor(tresor_x: int, tresor_y: int) -> tuple[bool, int, int]:
    x = 0
    y = 0
    instruccions = 0
    total_passes = 0

    direccio = yogi.scan(str)

    while direccio:
        pas_a_pas = False
        passes = yogi.read(int)

        # Comprovar que no ens passem el tresor
        if (direccio == "up" and y + passes > tresor_y) or (direccio == "down" and y - passes < tresor_y):
            pas_a_pas = True
        elif (direccio == "right" and x + passes > tresor_x) or (direccio == "left" and x - passes < tresor_x):
            pas_a_pas = True

        instruccions += 1

        if pas_a_pas: # Moure pas a pas
            for _ in range(1, passes + 1):
                total_passes += 1
                x, y = moure_robot(x, y, direccio, 1)

                if x == tresor_x and y == tresor_y:
                    return True, instruccions, total_passes
        else: # Moure totes les passes de cop
            total_passes += passes
            x, y = moure_robot(x, y, direccio, passes)

            if x == tresor_x and y == tresor_y:
                return True, instruccions, total_passes

        direccio = yogi.scan(str)

    return False, instruccions, total_passes


def moure_robot(x0: int, y0: int, direccio: str, passes: int) -> tuple[int, int]:
    if direccio == "up":
        return x0, y0 + passes
    elif direccio == "down":
        return x0, y0 - passes
    elif direccio == "right":
        return x0 + passes, y0
    else:
        return x0 - passes, y0


def main() -> None:
    tresor_x = yogi.read(int)
    tresor_y = yogi.read(int)

    resultat_tresor = trobar_tresor(tresor_x, tresor_y)

    if not resultat_tresor[0]:
        print("not found", end=" ")

    print(resultat_tresor[1], resultat_tresor[2])


if __name__ == "__main__":
    main()
