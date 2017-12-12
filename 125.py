#!/usr/bin/env python3
__author__ = "Christian F. Walter"

def palindrome(n):
  return str(n) == str(n)[::-1]

if __name__ == "__main__":
  # n = 32
  n = 10000
  squares = [i**2 for i in range(1, n)]

  total = 0
  num = 0
  for i in range(2,n):
    for j in range(i-1):
      s = sum(squares[j:i])
      if s < 100000000 and palindrome(s):
        total += s
        num += 1
        # print('[{}:{}]'.format(j,i), s)

  print('*'*16)
  print(total, num)
