from math import sqrt
from itertools import combinations

thousand = 1000
t_sum = [0 for i in range(thousand + 1)]

for a, b in combinations(range(1, thousand), 2):
    c = sqrt(a**2 + b**2)
    p = int(a+b+c)
    if c.is_integer() and p <= 1000:
        t_sum[p] += 1

max_sum = 0
max_key = 0
for key, val in enumerate(t_sum):
    if val > max_sum:
        max_sum = val
        max_key = key
