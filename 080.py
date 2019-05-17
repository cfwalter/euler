from decimal import *
getcontext().prec = 102

print(sum(sum(int(Decimal(n).sqrt() * 10**i)%10 for i in range(100)) for n in range(101) if Decimal(n).sqrt() % 1))
