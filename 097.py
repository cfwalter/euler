n = 1
d = 10**10
for i in range(7830457):
    n = (n*2) % d

n = (28433 * n + 1) % d
