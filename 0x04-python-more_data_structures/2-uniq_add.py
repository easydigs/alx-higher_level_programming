#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    number = 0

    for index in uniq_list:
        number += index

    return (number)
