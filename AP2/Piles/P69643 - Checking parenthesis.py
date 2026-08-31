import yogi

def parenthesization_check(word: str) -> bool:
    '''Donat una seqüència de parèntesis, retorna "True" si tots els parèntesis
    estan correctament tancats, retorna "False" alternament.'''

    pila = list[str]()

    for par in word:
        if par == "(" or par == "[": # if par in "(["
            pila.append(par)
        elif par == ")":
            if len(pila) == 0 or pila.pop() != "(":
                return False
        elif par == "]":
            if len(pila) == 0 or pila.pop() != "[":
                return False
        else:
            assert False, "Incorrect input!, expected '(, [, ) ]'."

    return len(pila) == 0

def main() -> None:
    entrada = yogi.scan(str)
    while entrada is not None:
        entrada.replace(" ", "")
        if entrada == "":
            continue
        elif parenthesization_check(entrada):
            print(f"{entrada} is correct")
        else:
            print(f"{entrada} is incorrect")
        entrada = yogi.scan(str)

if __name__ == "__main__":
    main()