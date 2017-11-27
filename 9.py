#!/usr/bin/env python3
__author__ = "Christian F. Walter"
import math
from functools import reduce
from operator import mul

if __name__ == "__main__":
  for i in range(30):
    for j in range(i):
      if (i**2 + j**2
