#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import sqrt

def abundant(n):
  total = 0
  sn = sqrt(n)
  for i in range(2, int(sn + 1)):
    if n % i == 0 and i != sn:
      total += i
      total += n//i
  if sn.is_integer(): total += sn
  return total + 1 > n

def sum_pairs(l):
  sum_l = []
  for i in l:
    for j in l:
      sum_l.append(i+j)

  return set(sum_l)

if __name__ == "__main__":
  ab = []
  upper = 28123
  for n in range(10, upper):
    if abundant(n): ab.append(n)

  all_num = set(range(upper + 1))
  print(sum(all_num - sum_pairs(ab)))