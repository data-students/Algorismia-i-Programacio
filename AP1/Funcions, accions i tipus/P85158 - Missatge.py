def missatge(qui: str, verb: str, cops: int, fem: bool) -> None:
    if fem:
        print ("Na", qui, end=" ")
    else:
        print ("En", qui, end= " ")
    
    if cops == 0:
        print ("no ha", verb, end= ".\n")

    else:
        print ("ha", verb, cops, end = " ")
        if cops == 1:
            print ("cop.")
        else: 
            print ("cops.")