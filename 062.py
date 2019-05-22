from collections import defaultdict

n = 5
cubes = defaultdict(list)
for i in range(10000):
    key = ''.join(sorted(str(i**3)))
    cubes[key].append(i**3)
    if len(cubes[key]) == n:
        print(cubes[key])
