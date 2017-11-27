#!/usr/bin/env python3
# WIP
__author__ = "Christian F. Walter"
import math

def is_prime(n, primes):
  s = math.sqrt(n)
  for p in primes:
    if n % p == 0:
      return False
    if p > s:
      return True
  return True

if __name__ == "__main__":
  primes = []
  p_factors = []
  for n in range(2,600851475143):
    if n % 100000 == 0:
      print(n)
    if is_prime(n, primes):
      primes.append(n)
      if 600851475143 % n == 0:
        p_factors.append(n)

  print('*' * 8)
  print(p_factors[-1])

