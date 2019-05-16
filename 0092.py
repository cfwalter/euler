def sum_digits_sq(n):
   r = 0
   while n:
       r, n = r + (n % 10)**2, n // 10
   return r

def num_chain_89(n):
    m = sum_digits_sq(n)
    if n == 1:
        return False
    if n == 89:
        return True
    return num_chain_89(m)


n = 0
for i in range(2, 10**7):
    n += 1 if num_chain_89(i) else 0
