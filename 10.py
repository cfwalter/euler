#!/usr/bin/env python3
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
  for n in range(2,2000000):
    if n % 1000 == 0:
      print(n)
    if is_prime(n, primes):
      primes.append(n)

  print(sum(primes))

