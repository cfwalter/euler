#!/usr/bin/env python3
__author__ = "Christian F. Walter"

def d(n):
  divisors = []
  for i in range(1, n/2 + 1):
    if n % i == 0:
      divisors.append(i)
  return sum(divisors)

if __name__ == "__main__":
  total = 0
  for n in range(1, 10000):
    dn = d(n)
    if dn > n:
      if d(dn) == n:
        print(dn, n)
        total += n + dn

  print(total)
