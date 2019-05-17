from itertools import product

len([(base, power) for base, power in product(range(1, 22), repeat=2) if 10**(power-1) <= base**power < 10**power])
