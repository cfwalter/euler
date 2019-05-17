from math import log10

def is_permute(n):
    l = [''.join(sorted(str(n*i))) for i in range(1,7)]
    return l.count(l[0]) == len(l)


for i in range(1, 100000):
    # only check numbers that start with 1
    n = 10**int(log10(i)+1) + i
    if is_permute(n):
        print(n)
