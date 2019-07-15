def frac(n):
    return 1 if n % 3 != 2 else 2*((n+1)//3)

def frac_iter(n):
    num0 = 2
    num1 = 3
    for i in range(2, n):
        num0, num1 = num1, num0 + num1 * frac(i)
    return num1

sum([int(c) for c in str(frac_iter(100))])
