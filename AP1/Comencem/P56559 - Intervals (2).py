from yogi import read

a1 = read (int)
b1 = read (int)
a2 = read (int)
b2 = read (int)

if (a1 == a2) and (b1 == b2):
    print ("=")

elif a2 <= a1 <= b1 <= b2:
    print ("1")

elif a1 <= a2 <= b2 <= b1:
    print ("2")

else:
    print ("?")