import yogi

def are_primes(num1: int, num2: int) -> bool:
    '''Donat dos numeros, retorna "True" si els dos numeros son primers simulàniament. Retorna "False" alternament.'''

    i = 2
    while i*i <= num2:
        if num2 % i == 0 or num1 % i == 0:
            return False
        i += 1

    return True

def nth_twin_primes(n: int) -> tuple[int, int]:
    '''Donat un nombre n, retorna l'n-èssim parell de nombres primers bessons.'''
    twin_prime_number = 1
    num1 = 3
    num2 = 5
    while twin_prime_number != n:
        num1 += 2
        num2 += 2
        if are_primes(num1, num2):
            twin_prime_number += 1
    return num1, num2

def main() -> None:
    for n in yogi.tokens(int):
        solution = nth_twin_primes(n)
        print (solution[0], solution[1])

if __name__ == "__main__":
    main()