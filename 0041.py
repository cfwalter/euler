from itertools import permutations
import math

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


for p in permutations(range(7, 0, -1)):
    n = int(''.join(map(str, p)))
    if is_prime(n):
        print(n)
