#!/usr/bin/python3
# 4-new_in_list.py
# When yo copy a tring using the '=' pyhton only creates a new name
# for the same data (refrences it). They share the same memory space
# But when yoy slice or use copy(It creates a new list all together)

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        newlist = my_list[:]
        newlist[idx] = element
        return newlist
