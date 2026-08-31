import yogi

def is_even (n: int) -> bool:
    return n % 2 == 0

def main():
    entrada = yogi.scan (int)
    pos_even = 0
    while entrada is not None:

        pos_even += 1

        if is_even(entrada):
            entrada = None
        else:
            entrada = yogi.scan (int)
    
    print (pos_even)

if __name__ == "__main__":
    main()