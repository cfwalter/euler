from math import log10

def phi_1_to_n(n):
    phi = [i for i in range(n)]
    for i in range(2,n):
        if phi[i] == i:
            for j in range(i, n, i):
                phi[j] -= phi[j] // i
    return phi

def is_permutation(x, y):
    if int(log10(x)) != int(log10(y)):
        return False
    dig_count = [0 for i in range(10)]
    while x:
        dig_count[x%10] += 1
        x = x//10;
    while y:
        dig_count[y%10] -= 1
        y = y//10;
    return not any(dig_count)


n = 10**7
phi = phi_1_to_n(n)
phi_ratio = [(i, i/phi[i]) for i in range(2,n) if is_permutation(i, phi[i])]
min_ratio = n
min_index = 0
for i, r in phi_ratio:
    if r < min_ratio:
        min_ratio = r
        min_index = i

print(f'{min_index}: {min_ratio}')
