#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import factorial

if __name__ == "__main__":
  total = 1
  n = 1
  skip = 2
  cap = 1001**2
  while n < cap:
    total += (n + skip) + (n + skip*2) + (n + skip*3) + (n + skip*4)
    n = (n + skip*4)
    skip += 2

  print(total)
