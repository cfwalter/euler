#!/usr/bin/env python3
__author__ = "Christian F. Walter"

from math import

# only works for n <= 1000
def getNumString(n):
  digits = {
    0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
    10: 'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',
    18:'eighteen', 19:'nineteen',
  }
  tens = {
    2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety', 
  }
  s = ''
  if n == 1000:
    return 'onethousand'
  if n >= 100:
    s += digits[n/100] + 'hundred'
    n = n % 100
    if n % 100:
      s += 'and'
  if n >= 20:
    return s + tens[n/10] + digits[n%10]
  return s + digits[n]

if __name__ == "__main__":
  sum = 0
  for n in range(1001):
    sum += len(getNumString(n))
  print(sum)
