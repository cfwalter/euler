x = 3/7
frac = (2, 7)
for d in range(1000000, 0, -1):
    if d % 7 == 0:
        continue
    n = int(x*d)
    if (n/d > frac[0]/frac[1]):
        frac = (n, d)

print(frac)
