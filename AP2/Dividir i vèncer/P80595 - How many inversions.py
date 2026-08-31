from yogi import read, tokens

def merge(left: list[int], right: list[int]) -> tuple[list[int], int]:
    """
    Fusiona dues llistes ordenades i compta el nombre de inversios que hi han entre elles.
    Prec: les dues llistes han d'estar ordenades.
    """
    ret: list[int] = []
    i = j = inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ret.append(left[i])
            i += 1
        
        else: # Si és major, tindrem len(left) - i inversions
            ret.append(right[j])
            inv_count += len(left) - i  # Totes les restants a 'left' son majors
            j += 1

    ret.extend(left[i:])
    ret.extend(right[j:])
    return ret, inv_count

def mergesort_adapt(L: list[int]) -> tuple[list[int], int]:
    """Utilitza un 'mergesort adaptat' per calcular el nombre de inersions d'una llista.
    Retorna la llista ordenada i el nombre de inversions."""
    if len(L) <= 1:
        return L, 0
    mid = len(L) // 2
    left, inv_left = mergesort_adapt(L[:mid])
    right, inv_right = mergesort_adapt(L[mid:])
    merged, inv_split = merge(left, right)
    return merged, inv_left + inv_right + inv_split

def inversions(L: list[int]) -> int:
    """Donada una llista, retorna el nombre de inversions que hi han."""
    _, total_inv = mergesort_adapt(L)
    return total_inv

def main() -> None:
    for n in tokens(int):
        elements = [read(int) for _ in range(n)]
        print(inversions(elements))
    

if __name__ == "__main__":
    main()