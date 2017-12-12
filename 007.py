#!/usr/bin/env python3
__author__ = "Christian F. Walter"
import math

def is_prime(n, primes):
  s = math.sqrt(n)
  for p in primes:
    if n % p == 0:
      return False
  return True

if __name__ == "__main__":
  primes = []
  n = 2
  while len(primes) < 10001:
    if is_prime(n, primes):
      primes.append(n)
    n += 1

  print(primes[-1])
  print(len(primes))

