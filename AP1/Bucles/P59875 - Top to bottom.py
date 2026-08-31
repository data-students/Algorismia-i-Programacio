from yogi import read

x, y = read (int), read (int)

if x >= y:
    i = x
    while i >= y:
        print (i)
        i -= 1

else:
    i = y
    while i >= x:
        print (i)
        i -= 1