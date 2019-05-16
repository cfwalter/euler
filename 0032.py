import itertools

products = []
for i, j in itertools.combinations(range(10000), 2):
    s = f'{i}{j}{i*j}'
    if ''.join(sorted(s)) == '123456789':
        products.append(i*j)

print(sum(set(products)))
