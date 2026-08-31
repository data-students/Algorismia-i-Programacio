import yogi

def val(c: str) -> int:
    return ord(c) - ord ('a') + 1

def car(n: int) -> str:
    return (chr(n + ord('a') - 1))

def anterior (c: str) -> str:
    return car (val (c) - 1)

def escriure_patro (c: str) -> None:
    if c == 'a':
        print('a', end='')
    elif c == "b":
        print ("bab", end='')
    elif c == "c":
        print ("cbabcbabc", end='')
    elif c == "d":
        print ("dcbabcbabcdcbabcbabcdcbabcbabcd", end='')
    elif c == "e":
        print ("edcbabcbabcdcbabcbabcdcbabcbabcdedcbabcbabcdcbabcbabcdcbabcbabcdedcbabcbabcdcbabcbabcdcbabcbabcdedcbabcbabcdcbabcbabcdcbabcbabcde", end='')
    else:
        v = val(c)
        for _ in range (v - 1):
            print(c, end='')
            escriure_patro (anterior(c))
        print (c, end='')

def main() -> None:
    c = yogi.read(str)
    escriure_patro(c)
        
    print()

if __name__ == "__main__":
    main()





'''
def lletres_a_index (n: str) -> int:

    lletres = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    index_lletres = (1, 2, 3, 4, 5, 6, 7)
    
    index_Entrada = 0

    for i in range (10):
        if n == lletres [i]:
            index_Entrada = index_lletres [i]
    
    return index_Entrada
    
def patro (entrada: int) -> None:

    lletres = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    if entrada == 1:
        print ('a', end='')
    else:
        for _ in range (entrada):
            print (lletres[entrada - 1])
            patro(entrada - 1)
        
        print (lletres[entrada - 1])
        

def main() -> None:
    while True:
        entrada = lletres_a_index (yogi.read(str))
        patro(entrada)

if __name__ == "__main__":
    main()
'''
