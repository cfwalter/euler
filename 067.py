#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import factorial

if __name__ == "__main__":
  with open('p067_triangle.txt', 'r') as tri_file:
    tri = tri_file.readlines()
    for i, row in enumerate(tri):
      tri[i] = row.strip().split()

  # # from bottom to top, sum max of two numbers below
  for row in range(len(tri)-1, 0, -1):
    for i, n in enumerate(tri[row-1]):
      tri[row-1][i] = int(n) + max(int(tri[row][i]), int(tri[row][i+1]))

  print(tri[0][0])
