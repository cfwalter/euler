from math import factorial
from itertools import combinations

def choose(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

len([(r,n) for r, n in combinations(range(1, 101), 2) if choose(n, r) > 10**6])
