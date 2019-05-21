def factors(n, primes):
    f = []
    for i in primes:
        if i*2 > n:
            return f
        if n%i == 0:
            f.append(i)
    return f

def is_prime(n):
    return not bool([i for i in range(2, int(n**(1/2)+1)) if n % i == 0])

n = 134050
x=4
primes = [i for i in range(2, n//2) if is_prime(i)]

l = [i for i in range(2, n) if len(factors(i, primes))==x]

for ind in range(len(l) - x):
    if all(l[ind+i]==l[ind]+i for i in range(1, x)):
        print(l[ind])
