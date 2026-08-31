from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class Provincia:
    nom: str
    capital: str
    habitants: int
    area: int
    pib: float

@dataclass
class Pais:
    nom: str
    capital: str
    provincies: list[Provincia]

Paisos: TypeAlias = list[Pais]

def habitants(paisos: Paisos, x: float) -> int:
    '''Retorna la suma de tots els habitats d'aquells paisos que tinguin almenys 2 provinies amb un pib igual o inferior a x.'''
    suma_total = 0
    for pais in paisos:
        suma_parcial = 0
        provincies_x_habitants = 0
        for provincia in pais.provincies:
            if provincies_x_habitants < 2 and provincia.pib <= x:
                provincies_x_habitants += 1
            suma_parcial += provincia.habitants
        if provincies_x_habitants == 2:
            suma_total += suma_parcial
    
    return suma_total