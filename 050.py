#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import sqrt

def is_prime(n, primes):
  s = sqrt(n)
  for p in primes:
    if n % p == 0:
      return False
    if p > s:
      return True
  return True

if __name__ == "__main__":
  winner = 0
  terms = 0
  total = 5
  primes = [2,3]
  n = 5
  while total < 1000:
    if is_prime(n, primes):
      primes.append(n)
      total += n
    if is_prime(total, primes):
      terms = len(primes)
      winner = total
    n += 2

  i = 0
  while i+terms <= len(primes):
    print('[{}:{}]'.format(i, i+terms))
    if is_prime(sum(primes[i:i+terms]), primes):
      winner = sum(primes[i:i+terms])
    i += 1

  print(primes)
  print(winner)