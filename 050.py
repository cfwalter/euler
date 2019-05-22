from itertools import combinations

def is_prime(n, primes):
    for i in primes:
        if i**2 > n:
            return True
        if n % i == 0:
            return False
    return True

def gen_primes(n):
    primes = [2,3,5,7]
    for i in range(11, n):
        if is_prime(i, primes):
            primes.append(i)
    return primes

n = 10**6
primes = gen_primes(n)

max_seq = (0,0)
s_p = set(primes)
for i,j in combinations(range(600), 2):
    s = sum(primes[i:j]) if j-i > max_seq[1]-max_seq[0] else 0
    if s < n and s in s_p:
        max_seq = (i, j)

sum(primes[max_seq[0]:max_seq[1]])
