#!/usr/bin/env python3

__author__ = "Christian F. Walter"
from math import factorial, log10

def is_fact(n, facts):
  total = 0
  for i in range(int(log10(n))+1):
    d = (n//10**i) % 10
    total += facts[d]
  return total == n

if __name__ == "__main__":
  facts = [factorial(i) for i in range(10)]
  # 2783915460 = 7 * 9!, therefore we only need 7 digits
  total = 0
  for i in range(9, 10000000):
    if is_fact(i, facts):
      total += i

  print('**', total)