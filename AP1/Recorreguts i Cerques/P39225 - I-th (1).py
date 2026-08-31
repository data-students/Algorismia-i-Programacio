import yogi

def main() -> None:
    desired_position = yogi.read (int)
    position = 0

    entrada = yogi.scan (int)
    while entrada is not None:
        position += 1
        
        if position == desired_position:
            print (f'At the position {desired_position} there is a(n) {entrada}.')
            entrada = None
        else:
            entrada = yogi.scan (int)

if __name__ == "__main__":
    main()