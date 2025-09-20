#!/usr/bin/python3
def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or not roman_string:
        return 0

    values = {'I': 1, 'V': 5, 'X': 10,
              'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = 0
    i = 0
    
    while i < len(roman_string):
        s1 = values[roman_string[i]]

        if i + 1 < len(roman_string):
            s2 = values[roman_string[i + 1]]
            if s1 >= s2:
                res += s1
                i += 1
            else:
                res += s2 - s1
                i += 2
        else:
            res += s1
            i += 1

    return res
