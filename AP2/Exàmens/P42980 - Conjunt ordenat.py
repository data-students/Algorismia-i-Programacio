"""COSTOS ASIMPTOTICS:
inserir(): O(n) en el pitjor cas (en el cas de que l'arbre estigui mal balancejat), O(logn) si estigués balancejat
conte(): O(1)
esborrar(): O(n) en el pitjor cas (en cas de que l'arbre estigui mal balancejat), O(logn) si estigués balancejat
entre(): O(n) en el pitjor cas
len(): O(1)
"""
from __future__ import annotations
import yogi
from typing import Iterator
from dataclasses import dataclass

@dataclass
class Node:
    dada: int
    esq: ArbreBin
    dre: ArbreBin

ArbreBin = Node | None

class ConjuntOrdenat:
    arbre: ArbreBin # arbre binari de cerca
    elements: set[int] # conjunt de valors a l'arbre binari

    def __init__(self) -> None:
        """Inicialitza el conjunt buit."""
        self.arbre = None
        self.elements = set()

    def inserir(self, x: int) -> None:
        """Insereix l'element x al conjunt. Si x ja hi és, no fa res."""

        def insereix_arbre_bin(arbre: ArbreBin, x: int) -> ArbreBin:
            """Insereix l'element x a un arbre binari donat.
            Prec: x no s'ha de trobar ja dins l'arbre"""

            # Cas base: l'arbre està buit
            if arbre is None:
                return Node(x, None, None)

            # Casos inductius: cercar on podria anar x (a la branca dreta o a la esquerra)
            elif x < arbre.dada:
                return Node(arbre.dada, insereix_arbre_bin(arbre.esq, x), arbre.dre)
            else:
                return Node(arbre.dada, arbre.esq, insereix_arbre_bin(arbre.dre, x))

        if x not in self.elements:
            self.elements.add(x)
            self.arbre = insereix_arbre_bin(self.arbre, x)
                
        
    def conte(self, x: int) -> bool:
        """Retorna 'True' si x es troba dins el conjunt, retorna 'False' alternament."""
        return x in self.elements


    def esborrar(self, x: int) -> None:
        """Esborra l'element x del conjunt. Si x no hi és, no fa res."""

        def esborra_arbre_bin(arbre: ArbreBin, x: int) -> ArbreBin:
            """Esborra l'element x de l'arbre binari.
            Prec: x s'ha de trobar dins del arbre binari."""

            assert arbre is not None
            # Casos base: Trobem x
            if x == arbre.dada:
                # Cas 1: No té fills
                if arbre.esq is None and arbre.dre is None:
                    return None

                # Cas 2: Té exactament un fill
                elif not (arbre.esq and arbre.dre):
                    return arbre.esq or arbre.dre

                # Cas 3: Té 2 fills
                else:
                    min_dre = min_arbre_bin(arbre.dre)
                    return Node(min_dre, arbre.esq, esborra_arbre_bin(arbre.dre, min_dre))

            # Casos inductius: Cercar x a l'arbre binari 
            elif x < arbre.dada:
                return Node(arbre.dada, esborra_arbre_bin(arbre.esq, x), arbre.dre)
            else:
                return Node(arbre.dada, arbre.esq, esborra_arbre_bin(arbre.dre, x))
                
        
        def min_arbre_bin(arbre: ArbreBin) -> int:
            """Retorna l'element minim d'un arbre binari donat."""
            assert arbre is not None
            if arbre.esq:
                return min_arbre_bin(arbre.esq)
            return arbre.dada

        if x in self.elements:
            self.elements.remove(x)
            self.arbre = esborra_arbre_bin(self.arbre, x)

    def entre(self, x: int, y: int) -> Iterator[int]:
        """Retorna un iterador que permet recórrer els elements 
        entre x i y (inclosos, amb x < y) del conjunt en ordre ascendent."""

        def entre_arbre_bin(arbre: ArbreBin, x: int, y: int) -> Iterator[int]:
            # Cas base: l'arbre està buit
            # Casos inductius:
            if arbre is not None:
                # Cas 1: x i y es troben dins l'interval, retornem en in-ordre
                if x <= arbre.dada <= y:
                    yield from entre_arbre_bin(arbre.esq, x, y)
                    yield arbre.dada
                    yield from entre_arbre_bin(arbre.dre, x, y)

                # Cas 2: x i y no es troben dins l'interval, fem cerca dins l'arbre
                elif x > arbre.dada:
                    yield from entre_arbre_bin(arbre.dre, x, y)
                elif y < arbre.dada:
                    yield from entre_arbre_bin(arbre.esq, x, y)

        assert x < y
        yield from entre_arbre_bin(self.arbre, x, y)


    def __len__(self) -> int:
        """Retorna el nombre d'elements al conjunt."""
        return len(self.elements)

def main() -> None:
    conjunt = ConjuntOrdenat()
    for comanda in yogi.tokens(str):
        if comanda == "inserir":
            conjunt.inserir(yogi.read(int))
        elif comanda == "conte":
            print(conjunt.conte(yogi.read(int)))
        elif comanda == "esborrar":
            conjunt.esborrar(yogi.read(int))
        elif comanda == "entre":
            print(*list(conjunt.entre(yogi.read(int), yogi.read(int))), sep=", ")
        elif comanda == "mida":
            print(len(conjunt))


if __name__ == "__main__":
    main()