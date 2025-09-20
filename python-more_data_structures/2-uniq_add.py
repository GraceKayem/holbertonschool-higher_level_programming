#!/usr/bin/python3
def uniq_add(my_list=[]):
    counts = []
    for add in my_list:
        if add not in counts:
            counts.append(add)
    return sum(counts)
