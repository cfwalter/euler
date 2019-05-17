import itertools
from functools import reduce
from fractions import Fraction

def cancel_digits(x, y):
    x_d = x // 10, x % 10
    y_d = y // 10, y % 10
    if x_d[0] in y_d:
        return x_d[1], y_d[0] if y_d[1] == x_d[0] else y_d[1]
    elif x_d[1] in y_d:
        return x_d[0], y_d[0] if y_d[1] == x_d[1] else y_d[1]
    else:
        return None

product = Fraction(1,1)
for num, den in itertools.combinations(range(11,100), 2):
    if num % 10 == 0 or den % 10 == 0:
        continue
    cancelled = cancel_digits(num, den)
    if cancelled is not None:
        f = Fraction(cancelled[0], cancelled[1])
        if Fraction(num, den) == f:
            print(f'{num}/{den} = {f}')
            product *= f

print(product)
