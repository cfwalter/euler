n =1000001
totals = [i-1 for i in range(n)]
for d in range(1, n):
    for i in range(2*d, n, d):
        totals[i] -= totals[d]

print(sum(totals) + 1)
