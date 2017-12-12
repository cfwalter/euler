#!/usr/bin/env python3
__author__ = "Christian F. Walter"

first_days_reg = [
  1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335
]
first_days_leap = [
  1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336
]

# 0=monday, 1=t, 2=w, 3=th, 4=f, 5=sat, 6=sun
def first_sundays_by_jan_1(n, leap):
  if leap:
    l = first_days_leap
  else:
    l = first_days_reg
  total = 0
  for d in l:
    if (d+n)%7 == 0:
      total += 1
  return total

def is_leap_year(yr):
  if yr%400 == 0:
    return True
  if yr%100 == 0:
    return False
  if yr%4 == 0:
    return True
  return False

if __name__ == "__main__":
  # jan1, 1901 is a tuesday
  jan1 = 1
  total = 0
  for yr in range(1901, 2001):
    print(yr,)
    leap = is_leap_year(yr)
    total += first_sundays_by_jan_1(jan1, leap)
    if leap:
      jan1 = (jan1+2)%7
    else:
      jan1 = (jan1+1)%7

  print(total)
