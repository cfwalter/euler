from itertools import permutations

n = 5
magic_nums = []
for c in permutations(list(range(1, n*2+1)), n*2):
    if 10 not in c[0:3]:
        # little optimization for ya
        continue
    sl = [[c[i], c[i%n+n], c[(i+1)%n+n]] for i in range(n)]
    if min([s[0] for s in sl]) == sl[0][0]:
        if len(set([sum(s) for s in sl])) == 1:
            magic_nums.append(int(''.join([''.join([str(c) for c in s]) for s in sl])))
