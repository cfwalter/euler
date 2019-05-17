from math import log10
from itertools import product

def sum_digits(n):
   return sum((n // 10**i) % 10 for i in range(int(log10(n)+1)))

max([sum_digits(a**b) for a,b in product(range(1, 100), repeat=2)])
