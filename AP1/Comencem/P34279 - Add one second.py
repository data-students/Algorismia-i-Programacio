from yogi import read

h0 = read (int)
m0 = read (int)
s0 = read (int)

s0 += 1

if s0 == 60:
    s0 = 0
    m0 += 1

if m0 == 60:
    m0 = 0
    h0 += 1

if h0 == 24:
    h0 = 0

if h0 <= 9:
    print ("0", sep ="", end = "")
print (h0, ":", sep ="", end = "")
if m0 <= 9:
    print ("0", sep ="", end = "")
print (m0, ":", sep ="", end = "")
if s0 <= 9:
    print ("0", sep ="", end = "")
print (s0)
