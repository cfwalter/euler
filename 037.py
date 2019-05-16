from math import sqrt, log10


def is_prime(n, prime_list):
    if n == 1:
        return False
    sqrt_n = sqrt(n)
    if n in set(prime_list):
        return True
    for p in prime_list:
        if n % p == 0:
            return False
        if p >= sqrt_n:
            return True

def truncates(n):
    l = [n%10**(i+1) for i in range(int(log10(n)))]
    r = [n//10**(i+1) for i in range(int(log10(n)))]
    return l + r

primes = [2,3,5,7]
t_primes = []
for i in range(11, 3798, 2):
    if is_prime(i, primes):
        primes.append(i)
        if all([is_prime(t, primes) for t in truncates(i)]):
            t_primes.append(i)

print(sum(t_primes))
