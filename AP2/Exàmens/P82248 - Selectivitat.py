rom yogi import read
from dataclasses import dataclass
from typing import Optional


@dataclass
class Estudiant:
    nom: str
    dni: int
    nota: float
    preferencies: list[str]
    assignacio: Optional[str]


def llegir_estudiant() -> Estudiant:
    return Estudiant(read(str), read(int), read(float), read(str).split(','), None)


def llegir_estudiants() -> list[Estudiant]:
    return [llegir_estudiant() for _ in range(read(int))]


@dataclass
class Titulacio:
    nom: str
    places: int
    nota_de_tall: float


def llegir_titulacio() -> Titulacio:
    return Titulacio(read(str), read(int), 0.0)


def llegir_titulacions() -> list[Titulacio]:
    return [llegir_titulacio() for _ in range(read(int))]


def assignar(estudiants: list[Estudiant], titulacions: list[Titulacio]) -> None:
    """Els estudiants es processen segons la seva nota (de la més alta a la més baixa, 
    i de DNI més baix a DNI més alt en cas d’empat per nota). Cada estudiant és assignat 
    a la primera titulació de les seves preferències que encara tingui places lliures. 
    Si cap de les seves titulacions preferides té places lliures, l’estudiant no reb cap assignació."""

    ord_estudiants = sorted(estudiants, key=lambda x: (-x.nota, x.dni)) # Ordenar primer per nota, (de més a menys). Després per dni (de menys a més)
    for estudiant in ord_estudiants:
        seguent = False
        for preferencia in estudiant.preferencies:
            for titulacio in titulacions:
                if preferencia == titulacio.nom and titulacio.places > 0:
                    estudiant.assignacio = preferencia
                    titulacio.places -= 1
                    titulacio.nota_de_tall = estudiant.nota
                    seguent = True
                    break
            if seguent:
                break

def escriure_assignacio(estudiants: list[Estudiant]) -> None:
    
    print("-"*3)
    ord_estudiants = sorted(estudiants, key=lambda x: (x.dni))
    for estudiant in ord_estudiants:
        print(estudiant.dni, estudiant.nom, estudiant.assignacio)


def escriure_notes_de_tall(titulacions: list[Titulacio]) -> None:
    """Dona, per cada titulació, el seu nom, la seva nota de tall i 
    el nombre de places lliures, i està ordenat per nota de tall decreixent 
    (i per ordre alfabètic del nom de la titulació en cas d’empat)."""
    
    print("-"*3)
    ord_titulacions = sorted(titulacions, key=lambda x: (-x.nota_de_tall, x.nom))
    for titulacio in ord_titulacions:
        print(titulacio.nom, titulacio.nota_de_tall, titulacio.places)

def main() -> None:
    estudiants = llegir_estudiants()
    titulacions = llegir_titulacions()
    assignar(estudiants, titulacions)
    escriure_assignacio(estudiants)
    escriure_notes_de_tall(titulacions)


if __name__ == '__main__':
    main()