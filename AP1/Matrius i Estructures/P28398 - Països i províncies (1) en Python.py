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

def pib(paisos: Paisos, inicial: str, densitat: float) -> float:
    '''
    Retorna la suma del pib de tots els amb una densitat estrictament superior a
    "densitat" i que comencim per la lletra "inicial".
    '''
    total_pib = 0.0
    for pais in paisos:
        if pais.nom[0] == inicial:
            for provincia in pais.provincies:
                provincia_densitat = provincia.habitants / provincia.area
                if provincia_densitat > densitat:
                    total_pib += provincia.pib
    
    return total_pib