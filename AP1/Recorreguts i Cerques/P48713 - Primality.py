import yogi

def es_primer(n: int) -> bool:
    if n <= 1:
        return False
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True

def main() -> None:
    nombres = yogi.read(int)
    nombres += 1
    for entrada in yogi.tokens (int):
        if es_primer (entrada):
            print (f'{entrada} is prime')
        else:
            print(f'{entrada} is not prime')

if __name__ == "__main__":
    main()