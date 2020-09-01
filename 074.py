from math import factorial

fact_dict = {i: factorial(i) for i in range(10)}
fact_chain = {
    0: 1, 1: 1, 2: 1,
    145: 1, 40585: 1,
    169: 3, 363601:3, 1454:3,
    871: 2, 45361:2,
    872: 2, 45362:2
}

def fact_sum(n):
    x = 0
    while n:
        x += fact_dict[n%10]
        n //= 10
    return x


def get_fact_chain(n):
    if n not in fact_chain:
        fact_chain[n] = get_fact_chain(fact_sum(n)) + 1
    return fact_chain[n]

count = 0
for i in range(1, 10**6):
    x = get_fact_chain(i)
    count += 1 if x == 60 else 0
print(count)
