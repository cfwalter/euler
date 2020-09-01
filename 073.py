from math import ceil, floor
n = 12001

totals = [0 for i in range(n)]

for d in range(2, n, 2):
    totals[d] -= 1

for d in range(3, n, 3):
    totals[d] -= 1

for d in range(1, n):
    x = ceil(d * 1/2) - floor(d * 1/3)
    totals[d] += x
    for i in range(2*d, n, d):
        totals[i] -= totals[d]

print(sum(totals[5:]))
