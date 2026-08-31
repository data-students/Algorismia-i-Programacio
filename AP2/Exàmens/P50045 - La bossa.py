import yogi
import heapq

class Bag:

    _k: int  # Repeticions máximes
    _repetitions: dict[int, int] # Clau: Enter, Valor: Nombre de vegades afeigit
    _pq_elements: list[int] # Emmagatzema sempre en la posició 0 l'element més petit
    _size: int # Nombre d'elements comptant possibles repeticions
    _items: int # Nombre d'elements sense comptar

    def __init__(self, k: int):
        """
        Crea una bossa buida de paràmere k.
        Prec: k >= 0

        El cost asimptòtic és constant (O(1)).
        """

        self._k = k
        self._repetitions = {}
        self._pq_elements = []
        self._size = 0
        self._items = 0

    def add(self, x: int) -> None:
        """
        Afegeix un enter a una bossa. Es poden afegir fins a k repeticions 
        de cada enter: Quan la bossa contingui k repeticions d'un cert enter, 
        afegir aquell enter no canvia la bossa.

        El cost asimptòtic és constant (O(1)).
        """

        if self._k == 0:
            return None

        # Si és la primera vegada que s'afageix a la bossa
        if x not in self._repetitions:
            self._repetitions[x] = 0
            heapq.heappush(self._pq_elements, x)
            self._items += 1

        # Si s'ha afeigit menys de k vegades, es contabilitza
        if self._repetitions[x] < self._k:
            self._repetitions[x] += 1
            self._size += 1

    def empty(self) -> bool:
        """
        Retorna 'True' si la bossa és buida, retorna 'False' alternament.

        El cost asimptòtic és constant (O(1)).
        """

        return True if self.size() < 1 else False

    def size(self) -> int:
        """
        Retorna quants elements diferents (sense repeticions) hi ha a la bossa.

        El cost asimptòtic és constant (O(1))
        """

        return self._size

    def items(self) -> int:
        """
        Retorna quants elements hi ha a la bossa comptant possibles repeticions.

        El cost asimptòtic és constant (O(1)).
        """

        return self._items

    def minimum(self) -> int:
        """
        Obté l'element més petit de la bossa (si no és buida).
        
        El cost asimptòtic és logarítmic (O(log(n))), ja que utilitza una cua 
        de prioritat per tenir sempre a la posició 0 l'element més petit.
        """

        assert not self.empty(), "La llista està buida!" # Pot aixecar una excepció si la llista està buida
        
        return self._pq_elements[0]

    def remove_minimum(self) -> int:
        """
        Esborra l'element més petit de la bossa (si no és buida). L'operació
        d'esborrar només esborra una de les ocurrències de l'element mínim 
        en cas de tenir-ne repeticions.
        
        El cost asimptòtic és (O(log(n))). La part principal d'aquest codi té 
        cost constant, però s'utilitza la funció minimum(), la qual té cost O(log(n))
        """
        
        assert not self.empty(), "La llista està buida!" # Pot aixecar una excepció si la llista està buida
        
        minumim = self.minimum()
        if self._repetitions[minumim] == 1:
            # Si l'element que es vol esborrar no està repetit més vegades, cal eliminar-ho de la bossa
            del self._repetitions[minumim]
            heapq.heappop(self._pq_elements)
            self._items -= 1
            self._size -= 1
        else:
            self._repetitions[minumim] -= 1
            self._size -= 1
        
        return minumim

def main() -> None:
    """Programa principal"""
    bag = Bag(yogi.read(int))
    for command in yogi.tokens(str):
        if command == "add":
            bag.add(yogi.read(int))
        elif command == "remove_minimum":
            print(bag.remove_minimum())
        elif command == "minimum":
            print(bag.minimum())
        elif command == "size":
            print(bag.size())
        elif command == "empty":
            print(bag.empty())
        elif command == "items":
            print(bag.items())
        else:
            assert False


if __name__ == "__main__":
    main()