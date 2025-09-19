#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #empty list to host the result
    new_list = []
    #looping over each element of the list one at a time
    for item in my_list:
        #does item match the value i want to replace
        if item == search:
            new_list.append(replace) #if yes, print the new list
        else:
            new_list.append(item) #if no, publish the original list
    return new_list 
