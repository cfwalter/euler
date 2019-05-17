from functools import reduce
from math import log10

million = 1000000
s = ''.join(str(i) for i in range(million+1))
l = [int(s[10**i]) for i in range(int(log10(million)))]
print(reduce(lambda x,y: x*y, l))
