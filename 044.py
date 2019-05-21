from itertools import combinations

p_nums = set([n*(3*n-1)//2 for n in range(1, 10001)])

[(i,j) for i, j in combinations(p_nums, 2) if abs(i-j) in p_nums and (i+j) in p_nums]
