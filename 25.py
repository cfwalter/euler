#!/usr/bin/env python3
__author__ = "Christian F. Walter"

if __name__ == "__main__":
  a = 1
  b = 2
  n = 3
  while b <= 10**999:
    b = a + b
    a = b - a
    n += 1

  print(n)