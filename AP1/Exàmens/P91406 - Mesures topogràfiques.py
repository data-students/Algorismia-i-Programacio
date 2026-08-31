import yogi

def escriu_perfil(roques: int, neu: int) -> None:
    '''Escriu en pantalla la representació del perfil de la muntanya (X = roques, * = neu).'''
    print (f"{'X' * roques}", end='')
    print (f"{'.' * neu}")

def mesures_topografiques () -> None:
    '''Començant a altura 0, mesura pas a pas les mesures que es llegeixen i fa una representació del perfil 
    de la muntanya. Si en algun moment alguna de les alçades esdevè nevativa, dona un error i s'atura el programa.'''

    roques = 0
    neu = 0

    for increment_roques in yogi.tokens(int):
        increment_neu = yogi.read(int)

        roques += increment_roques
        neu += increment_neu

        if roques < 0 or neu < 0:
            print ("ERROR")
            return
        
        escriu_perfil(roques, neu)

if __name__ == "__main__":
    mesures_topografiques ()


