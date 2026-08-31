import yogi
def llegir_entrada_en_llista (n: int) -> list[int]:

    llista: list[int] = []
    for _ in range (n):
        entrada = yogi.read(int)
        llista.append(entrada)
    
    return llista

def equal_sum_if_rest (L: list[int], n: int) -> bool:
    '''Donada una llista L, retorn "True", si hi ha algun numero que sigui la suma de la resta.'''
    sum_of_rest = sum(L)

    for nombre in L:
        if nombre == sum_of_rest - nombre:
            return True
    
    return False
        
def main() -> None:
    for n in yogi.tokens(int):
        llista = llegir_entrada_en_llista(n)
        is_sum_of_the_rest = equal_sum_if_rest(llista, n)

        if is_sum_of_the_rest:
            print ("YES")
        else:
            print ("NO")

if __name__ == "__main__":
    main()