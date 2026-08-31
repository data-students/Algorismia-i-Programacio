import yogi

def conjugar(verb: str) -> list[list[str]]:
    '''Donat un verb, retorna la seva conjugació en present d’indicatiu, i en variant dialectal central.
    Prec: els verbs han de ser regulars'''
    arrel = list(verb[:(len(verb) - 2)])
    conjugacions = ['o', 'es', 'a', 'em', 'eu', 'en']
    ret: list[list[str]] = []
    for i in range(6):
        # c > qu, g > gu, j > g, qu > qü, gu > gü
        # Regles ortogràfiques:
        if arrel[-1] == 'c' and arrel[-2] == ',' and (i == 1 or 3 <= i <= 6):
            arrel.pop(-2)
            ret.append(arrel + [conjugacions[i]])
            arrel[-1] = ','
            arrel.extend(['c'])

        elif arrel[-1] == 'c' and (i == 1 or 3 <= i <= 6):
            arrel[-1] = 'qu'
            ret.append(arrel + [conjugacions[i]])
            arrel[-1] = 'c'

        elif arrel[-1] == 'g' and (i == 1 or 3 <= i <= 6):
            arrel[-1] = 'gu'
            ret.append(arrel + [conjugacions[i]])
            arrel[-1] = 'g'

        elif arrel[-1] == 'j' and (i == 1 or 3 <= i <= 6):
            arrel[-1] = 'g'
            ret.append(arrel + [conjugacions[i]])
            arrel[-1] = 'j'
        elif (arrel[-2] == 'q' or arrel[-2] == 'g') and arrel[-1] == 'u' and (i == 1 or 3 <= i <= 6):
            arrel[-1] = '"u'
            ret.append(arrel + [conjugacions[i]])
            arrel[-1] = 'u'
        # Si aquella conjugació és completament regular
        else:
            ret.append(arrel + [conjugacions[i]])
    return ret

def main() -> None:
    entrada = yogi.scan(str)
    while entrada is not None:
        llista_conjugacions = conjugar(entrada)
        print (f'{entrada}: {" ".join("".join(str(llista_conjugacions[i][j]) for j in range(len(llista_conjugacions[i]))) for i in range(6))}')
        entrada = yogi.scan(str)

if __name__ == "__main__":
    main()