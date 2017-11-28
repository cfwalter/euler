#!/usr/bin/env python3
# WIP
__author__ = "Christian F. Walter"

from datetime import datetime
from math import log10
from random import randint

def reverse_str(n):
  return n + int(str(n)[::-1])

def reverse_math(n):
  rev = 0
  l = int(log10(n))+1
  for i in range(l):
    rev += ((n//10**i) % 10) * (10**(l-i-1))
  return n + rev

if __name__ == "__main__":
  nums = [randint(10**9,10**10) for i in range(10**7)]
  print('.')
  start = datetime.now()
  for n in nums:
    reverse_math(n)
  print('math:', datetime.now() - start)

  for n in nums:
    reverse_str(n)
  print('str:', datetime.now() - start)
