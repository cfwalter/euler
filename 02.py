#!/usr/bin/env python3
__author__ = "Christian F. Walter"

if __name__ == "__main__":
  a = 1
  b = 2
  sum = 0
  while b <= 4000000:
    if b % 2 == 0:
      sum += b
      print(b)
    b = a + b
    a = b - a

  print(sum)

