import yogi

def es_creixent_decreixent(numero: int, base: int) -> bool:
    '''Donat un numero n i una base, retorna "True" si aquell numero en una base determinada es creixent-decreixent.
    Retorna "False" alternament.'''
    if numero < 100:
        return True
    
    llargada = len(str(numero))
    digit1 = (numero // (10 **(llargada - 1))) % 10
    digit2 = (numero // (10 ** (llargada - 2))) % 10
    digit3 = (numero // (10 ** (llargada - 3))) % 10

    if numero < 1000:
        return digit1 < digit3

    digit4 = (numero // (10**(llargada - 4))) % 10

    if digit1 > digit3:
        return False
    elif digit2 < digit4:
        return False
    else:
        numero_sense_2_digits = numero % (10 ** (llargada - 2))
        return es_creixent_decreixent (numero_sense_2_digits, base)

def main() -> None:
    base = yogi.read(int)
    while base is not None:
        numero = yogi.read(int)
        if es_creixent_decreixent(numero, base):
            print("YES")
        else:
            print ("NO")

        base = yogi.scan(int)

if __name__ == "__main__":
    while True:
        main()