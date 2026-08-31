from yogi import read

n = read(int)

i = 1

while i < n:
    print (" "*(n-i), end="")
    print ("*"*(2*i-1))
    i += 1

while i > 0:
    print (" "*(n-i), end="")
    print ("*"*(2*i-1))
    i -= 1