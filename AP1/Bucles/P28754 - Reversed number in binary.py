from yogi import read

n = read (int)
ndec = n
nbin = ''

if n == 0:
    nbin = '0'

while n > 0:
    if n % 2 == 0:
        nbin = nbin + '0'

    else:
        nbin = nbin + '1'
    
    n = n // 2

print (nbin)
