#!/usr/bin/env python3
__author__ = "Christian F. Walter"

def divisors(n):
  d = []
  for i in range(1, int(n/2+1)):
    if int(n) % i == 0: d.append(i)
  d.append(n)
  return d

if __name__ == "__main__":
  # use Dickenson's method, check if sum=1000
  # https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples#Dickson.27s_method
  for r in range(2,200,2):
    div = divisors(r**2 / 2)
    for d in div:
      s = d
      t = (r**2 / 2) / d
      if (r+s) + (r+t) + (r+s+t) == 1000:
        print((r+s), (r+t), (r+s+t))
        print((r+s) * (r+t) * (r+s+t))