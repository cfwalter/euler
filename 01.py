#!/usr/bin/env python3
__author__ = "Christian F. Walter"

if __name__ == "__main__":
  three = range(0, 1000, 3)
  five = range(0, 1000, 5)
  fifteen = range(0, 1000, 15)
  print(sum(three) + sum(five) - sum(fifteen))

