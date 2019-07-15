def gen_primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def diags(n):
    n = 2*n + 1
    return [(n)**2-i*(n-1) for i in range(1, 4)]

n = 30000
sp = set(gen_primes(n**2))

total_primes = 0
for i in range(1, n):
    for j in diags(i):
        total_primes += 1 if j in sp else 0
    if 4*i+1 >= 10*total_primes:
        print(2*i+1)
        break
