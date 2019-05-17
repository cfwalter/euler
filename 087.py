from itertools import product

def is_prime(n):
    return not bool([i for i in range(2, int(n**(1/2)+1)) if n % i == 0])

n = 50*10**6
square_root = n ** (1/2) + 1
cube_root = n ** (1/3) + 1
fourth_root = n ** (1/4) + 1
i_primes = [i for i in range(2, int(square_root)) if is_prime(i)]
j_primes = [i for i in range(2, int(cube_root)) if is_prime(i)]
k_primes = [i for i in range(2, int(fourth_root)) if is_prime(i)]

len(set(i**2 + j**3 + k**4 for (i,j,k) in product(i_primes, j_primes, k_primes) if i**2 + j**3 + k**4 < n))
