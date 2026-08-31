from yogi import read, tokens

def knapsack_dp(W: int, w_z: list[int], v_z: list[float]) -> list[float]:
    z = len(w_z)

    # Rellenar cache (indivisibles)
    cost_z = [0.0] * (W + 1)  # cost_z[i] indica el valor maximo que podemos conseguir con peso i
    for i in range(z):
        for w in range(W, w_z[i] - 1, -1):
            cost_z[w] = max(cost_z[w - w_z[i]] + v_z[i], cost_z[w])

    return cost_z


def knapsack_greedy(W: int, w_r: list[int], v_r: list[float]) -> list[float]:
    r = len(w_r)

    # Para cada cache, rellenar con los divisibles
    ratio_r = [v_r[i] / w_r[i] for i in range(r)]
    sorted_r = sorted(range(r), key=lambda x: -ratio_r[x])
    cost_r = [0.0] * (W + 1)
    for w in range(W + 1):
        rem_W = w
        for i in sorted_r:
            if w_r[i] <= rem_W:
                cost_r[w] += v_r[i]
                rem_W -= w_r[i]
            else:
                cost_r[w] += v_r[i] / w_r[i] * rem_W
                break

    cost_r.reverse()
    return cost_r


def max_valor(W: int, w_z: list[int], v_z: list[float], w_r: list[int], v_r: list[float]) -> float:
    cost_z = knapsack_dp(W, w_z, v_z) # Indivisibles (llaunes)
    cost_r = knapsack_greedy(W, w_r, v_r) # Divisibles (embotits)

    # Devolver el maximo de la suma de las 2
    return max(cost_z[i] + cost_r[i] for i in range(W + 1))


def main() -> None:
    for W in tokens(int):
        z = read(int)
        w_z: list[int] = []
        v_z: list[float] = []
        for _ in range(z):
            v_z.append(read(float))
            w_z.append(read(int))

        r = read(int)
        w_r: list[int] = []
        v_r: list[float] = []
        for _ in range(r):
            v_r.append(read(float))
            w_r.append(read(int))

        ret = max_valor(W, w_z, v_z, w_r, v_r)
        print(f'{ret:.04f}')


if __name__ == "__main__":
    main()
