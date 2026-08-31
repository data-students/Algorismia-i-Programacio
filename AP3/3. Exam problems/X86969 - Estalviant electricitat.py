from yogi import read, tokens

def calcula_min_cost(autonomia: list[int], productivitat: list[int], consum: list[int], d: int) -> float:

    n = len(autonomia)
    rendiment = [productivitat[i] / consum[i] for i in range(n)]
    candidats = sorted(range(n), key= lambda i: rendiment[i], reverse=True)

    prod_actual = 0
    cons_actual = 0.0
    for i in candidats:
        if prod_actual == d:
            break

        if prod_actual + autonomia[i] * productivitat[i] < d:
            prod_actual += autonomia[i] * productivitat[i]
            cons_actual += float(autonomia[i] * consum[i])
        else:
            rest = d - prod_actual
            prod_actual += rest
            cons_actual += rest / productivitat[i] * consum[i]
    
    return cons_actual

def main() -> None:
    for n in tokens(int):
        autonomia = [read(int) for _ in range(n)]
        productivitat = [read(int) for _ in range(n)]
        consum = [read(int) for _ in range(n)]
        d = read(int)

        min_cost = calcula_min_cost(autonomia, productivitat, consum, d)
        print(f"{min_cost:.04f}")

if __name__ == "__main__":
    main()