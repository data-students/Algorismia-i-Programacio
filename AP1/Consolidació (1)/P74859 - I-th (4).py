import yogi

def ith_4 (position: int) -> None:
    number = yogi.scan (int)
    real_positions = 0
    found_number = number
    found_ith = False

    while number != -1 and number is not None:
        real_positions += 1
        
        if real_positions == position:
            found_number = number
            found_ith = True

        number = yogi.scan(int)

    if found_ith:
            print (f'At the position {position} there is a(n) {found_number}.')
    else:
        print ("Incorrect position.")


def main() -> None:
    entrada = yogi.scan(int)
    while entrada is not None:
        ith_4(entrada)
        entrada = yogi.scan(int)

if __name__ =="__main__":
     main()
