#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
Last_digit_of = number

if (Last_digit_of > 5):
  print(f"Last digit of {number:d} and is greater than 5")
elif (Last_digit_of == 0):
  print(f"Last digit of {number:d} and is 0")
else:
  print(f"Last digit of {number:d} and is less than 6 and not 0")