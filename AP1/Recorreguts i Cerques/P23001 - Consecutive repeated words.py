import yogi

def main() -> None:
    word = yogi.scan (str)
    consecutive_repeated_word = 1
    highest_consecutive_repeated_word = 1

    for entrada in yogi.tokens(str):
        if entrada == word:
            consecutive_repeated_word += 1
            if consecutive_repeated_word > highest_consecutive_repeated_word:
                highest_consecutive_repeated_word = consecutive_repeated_word
        else:
            consecutive_repeated_word = 0
    
    print (highest_consecutive_repeated_word)

if __name__ == "__main__":
    main()
