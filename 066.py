def dio(d):
    mi = 0
    di = 1
    ai = int(d**0.5)
    a0 = ai
    numi = a0
    deni = 1
    numi_1 = 1
    deni_1 = 0
    while numi**2 - d*deni**2 != 1:
        mi = di * ai - mi
        di = (d - mi**2) // di
        ai = (a0 + mi) // di
        numi_2 = numi_1
        numi_1 = numi
        numi = ai*numi_1 + numi_2
        deni_2 = deni_1
        deni_1 = deni
        deni = ai*deni_1 + deni_2
    return numi

max_d = (0, 0)
n = 1000
squares = [i**2 for i in range(int(n**0.5)+1)]
nonsquares = [i for i in range(n+1) if i not in squares]

for d in nonsquares:
    x = dio(d)
    if x > max_d[0]:
        max_d = (x, d)
