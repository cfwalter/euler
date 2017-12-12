#!/usr/bin/env python3
__author__ = "Christian F. Walter"
import math

if __name__ == "__main__":
  n = 20
  primes = {
    2: 1,
    3: 1,
    5: 1,
    7: 1,
    11: 1,
    13: 1,
    17: 1,
    19: 1,
  }
  for i in range(2,n):
    for key in primes:
      l = math.log(i,key)
      if float(l).is_integer() and l > primes[key]:
        primes[key] = l

  product = 1
  for key in primes:
    product = product * key ** primes[key]
  print(product)
  print('*' * 10)
  print(primes)
