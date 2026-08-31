from yogi import read

def is_leap_year(year: int) -> bool:
    if year % 100 == 0:
        if (year // 100) % 4 == 0:
            return True
        else:
            return False
    
    if year % 4 == 0:
        return True
    
    return False

def numero_mes (m):
    num_mes = 0
    mesos = [
        "gener", "febrer", "marc", "abril", "maig", "juny", 
        "juliol", "agost", "setembre", "octubre", "novembre", "desembre"
    ]
    for i in range (0,12):
        if mesos[i] == m:
            num_mes = i + 1

    return num_mes

def dia_seguent(d, m, a):
    dies_maxims = 31
    mesos = [
        "gener", "febrer", "marc", "abril", "maig", "juny", 
        "juliol", "agost", "setembre", "octubre", "novembre", "desembre"
    ]
    
    num_mes = numero_mes (m)

    if num_mes == 2:
        if is_leap_year(a):
            dies_maxims = 29
        else:
            dies_maxims = 28

    elif num_mes in (4,6,9,11):
        dies_maxims = 30

    d += 1

    if d > dies_maxims:
        d = 1
        num_mes += 1

        if num_mes > 12:
            num_mes = 1
            a += 1
    
    return d, mesos[num_mes - 1], a

while True:
    e1, e2, e3 = read(int), read(str), read(int)
    print (dia_seguent(e1,e2,e3))