#!/usr/bin/env python3
__author__ = "Christian F. Walter"
import math

def primeFactors(n):
    i = 5
    sn = math.sqrt(n)
    while i < sn:
        while n % i== 0:
            print i
        i += 2

if __name__ == "__main__":
  primeFactors(600851475143)
