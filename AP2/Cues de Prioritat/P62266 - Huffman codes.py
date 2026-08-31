import heapq
import yogi
from typing import TypeAlias

Letter: TypeAlias = tuple[float, str, list[float], list[int]] #tuple[sumatotal, lletresinvolucrades, frequenciesindividuals, nrebits]
PQ: TypeAlias = list[Letter]

def main() -> None:
    # Llegir les entrades i frequencies
    _ = yogi.read(int)
    pq: PQ = [(freq, str(i), [freq], [0]) for i, freq in enumerate(yogi.tokens(float))]
    heapq.heapify(pq)

    while len(pq) > 1:
        # Agafar els dos ultims de la cua
        sumtot1, dig1, freq1, nrebits1 = heapq.heappop(pq)
        sumtot2, dig2, freq2, nrebits2 = heapq.heappop(pq)

        # Sumar les seves frequències totals i afeigir els dígits, frequencies i nivells que representen els dos ultims
        heapq.heappush(pq, (sumtot1 + sumtot2, dig1 + dig2, freq1 + freq2, [bit + 1 for bit in (nrebits1 + nrebits2)]))

    # Sumar terme a terme la frequencia relativa i treure el percentatge
    freq = pq[0][2]
    nrebits = pq[0][3]
    total_percentage = sum(f*n for f, n in zip(freq, nrebits)) / 100
    

    print(f"expected number of bits per letter: {total_percentage:.4f}")


if __name__ == "__main__":
    main()