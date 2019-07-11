from math import factorial
from itertools import combinations_with_replacement

def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def pascal_row(n):
    return [binom(n,k) for k in range(n+1)]

def is_prime(n, primes):
    for i in primes:
        if i**2 > n:
            return True
        if n % i == 0:
            return False
    return True

def gen_sq_primes(n):
    primes = [2,3,5,7]
    for i in range(11, n, 2):
        if is_prime(i, primes):
            primes.append(i)
    return [p**2 for p in primes]

def squarefree(n, p):
    if all([n%p!=0 for p in sqp]):
        return n
    else:
        return 0


l = [pascal_row(n) for n in range(51)]
s = set([item for sublist in l for item in sublist])
sqp = gen_sq_primes(52)
filtered_list = [squarefree(n, sqp) for n in s]
total = sum(filtered_list)
