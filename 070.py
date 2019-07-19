def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def gen_primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def gen_compounds(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [1] + [i for i in range(3, n) if not sieve[i] or i%2==0]

def totient(n, pl):
    sqn = n**0.5
    num = n
    den = 1
    for p in pl:
        if p > sqn:
            break
        if n % p == 0:
            num *= p-1
            den *= p
    return num // den

n = 10**7
pl = gen_primes(n)
cl = gen_compounds(n)
cl.remove(1)
pal_list = []
for i in cl:
    t = totient(i, pl)
    if is_permutation(i, t):
        pal_list.append((i, t))

min_ratio = 100
min_n = 0
for n, t in pal_listtoti:
    if n/t < min_ratio:
        min_ratio = n/t
        min_n = n
