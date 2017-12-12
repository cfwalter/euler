#!/usr/bin/env python3
# 0*10! + 2*9! + 6*8! + 6*7! + 2*6! + 5*5! + 1*4! + 2*3! + 2*2! + 0*1!
__author__ = "Christian F. Walter"
from math import factorial

def get_perm_fact_list(num, digits):
  s = str(digits)
  fact_list = []
  fact_sum = 0
  mod = False
  for i in range(len(s)-1,-1,-1):
    if mod == True:
      p = -1
    else:
      p = (num - fact_sum) // factorial(i)
      if (num - fact_sum) % factorial(i) == 0:
        mod = True
        p -= 1
    fact_list.append(p)
    fact_sum += p * factorial(i)
  return fact_list

def get_perm(digits, fact_list):
  s = sorted(str(digits))
  p = ''
  for f in fact_list:
    p += s.pop(f)
  return p

if __name__ == "__main__":
  # perms = [int(''.join(p)) for p in permutations('0123456789')]
  # perms[999999]
  n = 1000000
  digits = 1234567890
  l = get_perm_fact_list(n, digits)
  print(get_perm(digits, l))
