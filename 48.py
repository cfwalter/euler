#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import factorial

if __name__ == "__main__":
  n = sum([i**i for i in range(1, 1001)])
  print(n % 10**10)
