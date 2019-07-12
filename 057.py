from math import log10

num = 3
den = 2
total = 0
for i in range(2, 1001):
    num += 2*den
    den += num - 2*den
    total += 1 if int(log10(num)) > int(log10(den)) else 0
