from math import sqrt


def is_prime(n, prime_list):
    sqrt_n = sqrt(n)
    for p in prime_list:
        if n % p == 0:
            return False
        if p >= sqrt_n:
            return True


def is_goldbach(n, primes):
    sqrt_n = int(sqrt(n // 2))
    for i in primes:
        for j in range(1, sqrt_n + 1):
            if i + 2*j**2 == n:
                return True
    return False


primes = [3,5,7]

for i in range(9, 10000, 2):
    if not is_prime(i, primes):
        if not is_goldbach(i, primes):
            print('*****', i)
    else:
        primes.append(i)
