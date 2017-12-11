#!/usr/bin/env python3
# 0*10! + 2*9! + 6*8! + 6*7! + 2*6! + 5*5! + 1*4! + 2*3! + 2*2! + 0*1!
__author__ = "Christian F. Walter"
from math import factorial

if __name__ == "__main__":
  perms = [int(''.join(p)) for p in permutations('0123456789')]
  perms[999999]
