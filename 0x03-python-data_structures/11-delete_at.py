#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
# for index in range(len(my_list)):
# if index != idx:  # value compare to not add inx of interest
# new_list.append(my_list[index])  # create new list
    del my_list[idx]
    return my_list
