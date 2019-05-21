from itertools import combinations

def is_prime(n):
    return not bool([i for i in range(2, int(n**(1/2)+1)) if n % i == 0])

def is_perm(x, y):
    return sorted(str(x)) == sorted(str(y))

primes = set([i for i in range(10**3, 10**4) if is_prime(i)])
diffs = [(i, j, j+(j-i)) for i,j in combinations(primes, 2) if j+(j-i) in primes]
perms = [(i, j) for i, j in combinations(primes, 2) if is_perm(i, j)]
seqs = [(i, j, max(i,j)+abs(j-i)) for i,j in perms if max(i,j)+abs(j-i) in primes and is_perm(i, max(i,j)+abs(j-i))]
