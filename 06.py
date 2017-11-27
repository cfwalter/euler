#!/usr/bin/env python3
__author__ = "Christian F. Walter"
import math

if __name__ == "__main__":
  n = 100
  square_sum = 0
  sum = 0
  for i in range(101):
    square_sum += i*i
    sum += i

  print(sum**2 - square_sum)
