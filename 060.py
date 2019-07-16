from itertools import combinations, permutations

known_primes = set()

def gen_primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True

def is_prime(n):
    if n in known_primes:
        return True
    if n % 2 == 0:
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7)):
        known_primes.add(n)
        return True
    else:
        return False

def prime_pairs(l, n):
    return all(is_prime(int(str(p1) + str(p2))) for p1, p2 in permutations(l, 2))

n = 10000
p = gen_primes(n)
for i in gen_primes(n*100):
    known_primes.add(i)

p.remove(2)
p.remove(5)
for i, a in enumerate(p):
    for j, b in enumerate(p[i:]):
        if not prime_pairs([a,b]):
            continue
        for k, c in enumerate(p[j:]):
            if not prime_pairs([a,b,c]):
                continue
            for l, d in enumerate(p[k:]):
                if not prime_pairs([a,b,c,d]):
                    continue
                for m, e in enumerate(p[l:]):
                    if prime_pairs([a,b,c,d,e]):
                        print([a,b,c,d,e], sum([a,b,c,d,e]))
