# WIP
from math import log10, sqrt

def noEven(n):
  for p in range(int(log10(n))+1):
    if n / 10**p % 2 == 0:
      return False
  return True

def circularPrime(n, primes):
  for r in rotations(n):
    if r not in primes:
      return False
  return True

def getAllPrimes(n):
  primes = []
  for i in range(n):
    prime = True
    si = sqrt(i)


n = 0
i = 1
while i < 300:
if noEven(i):
    print(i)
    i += 2
