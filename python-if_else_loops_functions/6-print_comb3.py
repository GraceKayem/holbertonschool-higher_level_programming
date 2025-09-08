#!/usr/bin/python3
for number in range(0, 10):
  for reverse_digit in range(number + 1, 10):
    if number == 8 and reverse_digit == 9:
      print("{}{}".format(number, reverse_digit))
    else:
      print("{}{}".format(number, reverse_digit), end=", ")



for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")