def cont_frac_size(s):
    m0 = 0
    d0 = 1
    a0 = int(s**0.5)
    def fun(ai, di, mi):
        mj = di * ai - mi
        dj = (s - mj**2) // di
        aj = (a0 + mj) // dj
        if aj == 2*a0:
            return 1
        else:
            return 1 + fun(aj, dj, mj)
    return fun(a0, d0, m0)

total = 0
n = 10000
squares = [i**2 for i in range(int(n**0.5)+1)]
nonsquares = [i for i in range(n+1) if i not in squares]
for i in nonsquares:
    if cont_frac_size(i)%2:
        total += 1
