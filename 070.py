def factors(n, primes):
    f = []
    for i in primes:
        if i*2 > n:
            return f
        if n%i == 0:
            f.append(i)
    return f

def is_prime(n, primes):
    for i in primes:
        if i**2 > n:
            return True
        if n % i == 0:
            return False
    return True

def gen_primes(n):
    primes = [2,3,5,7]
    for i in range(11, n, 2):
        if is_prime(i, primes):
            primes.append(i)
    return primes

def is_perm(x, y)
    return ''.join(sorted(str(x))) = ''.join(sorted(str(y)))


def phi(n, primes):
    result = 1
    for i in primes:
        if i > n:
            return result
        if n % i == 0:
            result *= (n - n//n)  # avoid float multi

n = 100
primes = gen_primes(n)

