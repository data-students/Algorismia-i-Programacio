from yogi import read

n = read (int)

h = n // 3600
min = (n % 3600) // 60
sec = n % 60

print (h, min, sec)