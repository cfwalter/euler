def tri(n):
    return n * (n+1) // 2

def sq(n):
    return n*n

def pent(n):
    return n * (3*n-1) // 2

def hexa(n):
    return n * (2*n - 1)

def hept(n):
    return n*(5*n-3)//2

def octo(n):
    return n * (3*n - 2)

def is_cycle(l, n):
    return l[-1][0] % 100 == n[0] // 100 and n[1] not in [i[1] for i in l]

fun_list = [tri, sq, pent, hexa, hept, octo]

fig_list = []
for n in range(1, 141):
    fig_list.extend([(f(n), i) for i, f in enumerate(fun_list) if 999<f(n)<=9999])

set_list = []
for l0 in fig_list:
    for l1 in filter(lambda x: is_cycle([l0], x), fig_list):
        for l2 in filter(lambda x: is_cycle([l0,l1], x), fig_list):
            for l3 in filter(lambda x: is_cycle([l0,l1,l2], x), fig_list):
                for l4 in filter(lambda x: is_cycle([l0,l1,l2,l3], x), fig_list):
                    for l5 in filter(lambda x: is_cycle([l0,l1,l2,l3,l4], x), fig_list):
                        if is_cycle([l1,l2,l3,l4,l5], l0):
                            print([l0,l1,l2,l3,l4,l5], sum([i[0] for i in [l0,l1,l2,l3,l4,l5]]))

