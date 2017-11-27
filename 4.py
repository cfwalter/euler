#!/usr/bin/env python3
__author__ = "Christian F. Walter"
import sys

def palindrome(n):
  s = str(n)
  pal = True
  for i in range(int(len(s)/2)):
    if s[i] != s[-(i+1)]:
      pal = False
  return pal

if __name__ == "__main__":
  max = 0
  for i in list(range(999,0,-1)):
    for j in list(range(999,0,-1)):
      if palindrome(i*j) and i*j > max:
        max = i*j
  print(max)

