from yogi import read

def num_accepted_words(tr_0: list[int], tr_1: list[int], ac: list[int], m: int) -> list[int]:
    n = len(tr_0)
    ret: list[int] = []
    
    prev_num_words = [1] + [0] * (n - 1) # l'estat inicial
    ret.append(1 if ac[0] else 0)
    
    for _ in range(m): # paraules de longitud i
        num_words = [0] * n # nombre de paraules de longitud i que et porten el node v (inicialmente i = 0)
        for curr_state, w in enumerate(prev_num_words):
            if w == 0:
                continue
            for adj_state in tr_0[curr_state], tr_1[curr_state]:
                num_words[adj_state] += w

        ret.append(sum(num_words[ac_state] for ac_state in range(n) if ac[ac_state]))
        
        # Guardar el resultat per la següent iteració
        prev_num_words = num_words[:]

    return ret

def main() -> None:
    n = read(int)
    tr_0 = [read(int) for _ in range(n)]
    tr_1 = [read(int) for _ in range(n)]
    ac = [read(int) for _ in range(n)]
    m = read(int)

    num_words = num_accepted_words(tr_0, tr_1, ac, m)
    for w in num_words:
        print(w)

if __name__ == "__main__":
    main()