#!/usr/bin/env python3
__author__ = "Christian F. Walter"
from math import factorial

def binom(n,k):
  return factorial(n) / (factorial(k) * factorial(n-k))

if __name__ == "__main__":
  n = 20*2
  print(binom(n, n/2))

