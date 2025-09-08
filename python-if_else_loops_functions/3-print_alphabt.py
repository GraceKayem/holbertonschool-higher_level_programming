#!/usr/bin/python3
for alphabets in range(97, 123):
  if chr(alphabets) in ('p', 'e'):
    continue
  print("{}".format(chr(alphabets)), end="")
