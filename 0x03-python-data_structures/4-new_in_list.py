#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list.copy()
        if idx < 0 or idx > len(new_list) - 1:
            return None
        new_list[idx] = element
        return new_list
