#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import factorial

if __name__ == "__main__":
  s = str(factorial(100))
  total = 0
  for c in s:
    total += int(c)
  print(total)
