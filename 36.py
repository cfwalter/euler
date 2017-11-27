#!/usr/bin/env python3
__author__ = "Christian F. Walter"

def palindrome(n):
  return str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[:1:-1]

if __name__ == "__main__":
  total = 0
  for n in range(1, 1000000, 2):
    if palindrome(n):
      total += n

  print(total)
