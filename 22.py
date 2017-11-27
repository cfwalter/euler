#!/usr/bin/env python3
__author__ = "Christian F. Walter"

def alphaval(s):
  total = 0
  for c in s:
    total += ord(c) - ord('@')
  return total

if __name__ == "__main__":
  with open('p022_names.txt', 'r') as name_file:
    names = name_file.read().replace('"', '').split(',')
  names.sort()

  total = 0
  for i, name in enumerate(names):
    total += (i+1) * alphaval(name)

  print(total)
