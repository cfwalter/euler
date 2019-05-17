def is_pandigital(n):
    return ''.join(sorted(str(n))) == '123456789'

for i in range(9487, 9234, -1):
    if is_pandigital(100002 * i):
        print(100002 * i)
