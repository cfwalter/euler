p_nums = set()
h_nums = set()

def tri(n):
    return n*(n+1) // 2

def pen(n):
    return n*(3*n-1) // 2

def hex(n):
    return n*(2*n-1)

for i in range(100000):
    t = tri(i)
    p_nums.add(pen(i))
    h_nums.add(hex(i))
    if t in p_nums and t in h_nums:
        print(t, i)
