from yogi import read

a, b = read(int), read(int)

i = a
if a <= b:
    while i < b:
        print (f'{i},', end='')
        i += 1
    print (b)
else:
    print ()
