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

def six_dig_primes():
    p = gen_primes(10**6)
    return list(filter(lambda x: x>10**5, p))


def threepeat_dig(n):
    s = str(n)
    for c in s:
        if s.count(c) == 3 and s[-1] != c and c in ['0', '1', '2']:
            return (s, c)
    return None


def is_eight_fam(s, d, p):
    digs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    fam = [c for c in digs if int(s.replace(d, c)) in p]
    fam = [int(s.replace(d, c)) for c in digs if int(s.replace(d, c)) in p]
    return len(fam) == 8



p = six_dig_primes()
l = list(filter(lambda x:x, map(threepeat_dig, p)))
sp = set(p)
fam_primes = filter(lambda x: is_eight_fam(x[0], x[1], sp), l)
