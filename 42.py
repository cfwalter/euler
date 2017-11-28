#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import sqrt

def is_triangle(n):
    x = (sqrt(8*n + 1) - 1) / 2
    return x.is_integer()

def alphaval(s):
  total = 0
  for c in s:
    total += ord(c) - ord('@')
  return total

if __name__ == "__main__":
  with open('p042_words.txt', 'r') as word_file:
    words = word_file.read().replace('"', '').split(',')

  total = 0
  for word in words:
    total += 1 if is_triangle(alphaval(word)) else 0

  print(total)
