import yogi
from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class Usuari:
    """Representació d'un usuari a la xarxa social"""
    nom: str # Nom del usuari
    amics: list['Usuari'] # Llista d'amics directes
    
# Representació de la xarxa social
Xarxa: TypeAlias = dict[str, Usuari] # Clau: nom, Valor: Usuari

def amics_de_amics(xarxa: Xarxa, usuari: Usuari) -> int:
    """Donada una xarxa social i un usuari, retorna el nombre total d'amics del usuari i 
    els d'amics d'amics (tret d'ell mateix i sense repetits)."""

    llista_amics: set[str] = set()
    
    for amic in usuari.amics:
        # Afeigir als amics
        llista_amics.add(amic.nom)
        for amic_de_amic in amic.amics:
            # Afeigir als amics dels amics
            llista_amics.add(amic_de_amic.nom)

    # En cas de que tingui almenys un amic, es resta 1 eliminar el cas on s'és amic d'un mateix
    return len(llista_amics) - 1 if len(llista_amics) > 0 else 0

def llegir_usuaris(n: int) -> Xarxa:
    """Donat un nombre n, es llegeix una llista de n paraules que corresponen als n noms d'usuari
    i els emmagatzema en la xarxa social."""

    xarxa: Xarxa = {}
    for _ in range(n):
        usuari = yogi.read(str)
        xarxa[usuari] = Usuari(usuari, [])
    return xarxa

def llegir_relacions(m: int, xarxa: Xarxa) -> None:
    """Donat un nombre m i una xarxa social, es llegeis la descripció 
    de les relacions d'amistat directes"""

    for _ in range(m):
        u1 = yogi.read(str)
        u2 = yogi.read(str)

        # Afeigir-se mutuament com a amics directes
        xarxa[u1].amics.append(xarxa[u2])
        xarxa[u2].amics.append(xarxa[u1])

def main() -> None:
    """Programa principal"""
    
    n, m = yogi.read(int), yogi.read(int)

    xarxa = llegir_usuaris(n)
    llegir_relacions(m, xarxa)

    for nom in yogi.tokens(str):
        usuari = xarxa[nom]
        print(amics_de_amics(xarxa, usuari))

if __name__ == "__main__":
    main()