from yogi import read

def floor (n):
    decimals = n % 1
    return int(n - decimals)

def day_of_the_week (d, m, y):
    m -= 2
    if m <= 0:
        m += 12
        y -= 1

    mp = m
    yp = y

    c = yp // 100

    a = yp % 100

    f = floor(2.6*mp-0.2) + d + a + floor (a/4) + floor (c/4) - 2*c

    num_dia = f % 7

    nom_dia = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    return nom_dia[num_dia]

while True:
    entrada1, entrada2, entrada3 = read(int), read(int), read(int)
    print (day_of_the_week(entrada1, entrada2, entrada3))