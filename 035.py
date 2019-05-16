from math import sqrt, log10


def is_prime(n, prime_list):
    sqrt_n = sqrt(n)
    if n in set(prime_list):
        return True
    for p in prime_list:
        if n % p == 0:
            return False
        if p >= sqrt_n:
            return True


def is_rot_prime(n, prime_list):
    len_n = int(log10(n))
    for i in range(len_n):
        n = (n%10 * 10**len_n) + n // 10
        if not is_prime(n, prime_list):
            return False
    # If we get this far, it is true
    return True


def has_25(n):
    # If number has 0,2,4,6,8 or 5 in the digits anywhere, its rotations will not be all prime
    s_n = str(n)
    bad_digits = '024685'
    return any(digit in s_n for digit in bad_digits)


primes = [2,3,5,7]
total = len(primes)  # single digit primes are all rot primes
million = 10**6

for i in range(11, million, 2)::
    if is_prime(i, primes):
        primes.append(i)
        if not has_25(i) and is_rot_prime(i, primes):
            total += 1

print(total)
