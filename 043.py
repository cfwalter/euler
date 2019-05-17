from itertools import permutations

def is_valid(s):
    primes = [2,3,5,7,11,13,17]
    if s[0] == '0':
        return False
    return all(int(s[i+1:i+4])%primes[i]==0 for i in range(len(primes)))

sum(int(''.join(n)) for n in permutations('0123456789', 10) if is_valid(''.join(n)))
