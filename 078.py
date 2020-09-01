mod = 10**6
n = 2
p = [1, 1]

while p[-1] != 0:
    j = 1
    k = 1
    part = 0
    while j < n:
        part += (-1)**(k+1) * p[n - j]
        k = k*-1 if k>0 else (k*-1)+1
        j = (k*(3*k-1))//2
    p.append(part % mod)
    n += 1

print(n)
