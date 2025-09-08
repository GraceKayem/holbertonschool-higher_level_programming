#!/usr/bin/python3
for number in range(0, 10):
  for reverse_digit in range(number + 1, 10):
    if number == 8 and reverse_digit == 9:
      print("{}{}".format(number, reverse_digit))
    else:
      print("{}{}".format(number, reverse_digit), end=", ")
