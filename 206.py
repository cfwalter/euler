#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import log10

if __name__ == "__main__":
  n = 1000000000
  powers = [(10-i, i*2) for i in range(1,10)]
  while n < 1414213562:
    if all(n**2//10**p[1] % 10 == p[0] for p in powers):
      print(n, n**2)
      break
    # target end in 0, so factors must be 2 and 5, stick to the tens
    n += 10
