#!/usr/bin/env python3
__author__ = "Christian F. Walter"
import math
from functools import reduce
from operator import mul

NUM = 2**1000

def sadd(a, b):
  return int(a) + int(b)

if __name__ == "__main__":
  s = reduce(sadd, str(NUM), 0)

  print(s)
