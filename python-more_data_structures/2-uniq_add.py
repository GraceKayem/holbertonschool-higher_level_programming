#!/usr/bin/python3
def uniq_add(my_list=[]):

    counts = []
    #counting the occurrences of each number
    for add in my_list:
        if add not in counts:
            counts.append(add)
    return sum(counts)
