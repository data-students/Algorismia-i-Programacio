from yogi import read, tokens

def canvi_minim(c: int, l: list[int]) -> str:

    l = sorted(l)
    cache = [-1] * (c + 1) # cache[i] indica el nombre minim de monedes per donar i diners
    cache[0] = 0 # cas base

    for cost in range(1, c + 1):
        for moneda in l:
            if moneda > cost: # poda (debil)
                break
            if cache[cost - moneda] != -1:
                if cache[cost] != -1:
                    cache[cost] = min(cache[cost - moneda] + 1, cache[cost])
                else:
                    cache[cost] = cache[cost - moneda] + 1

    return str(cache[c]) if cache[c] != -1 else "no"    

def main() -> None:
    for c in tokens(int):
        n = read(int)
        l = [read(int) for _ in range(n)]

        print(canvi_minim(c, l))

if __name__ == "__main__":
    main()