#!/usr/bin/env python3
__author__ = "Christian F. Walter"

def collatz_len(n):
  l = 1
  while n > 1:
    l += 1
    if n%2 == 0:
      n = n//2
    else:
      n = 3*n + 1
  return l

if __name__ == "__main__":
  winner_n = 0
  winner_l = 0
  for n in range(1, 10**6):
    if n % 1000 == 0: print(n)
    l = collatz_len(n)
    if l > winner_l:
      winner_n = n
      winner_l = l

  print(winner_n, winner_l)