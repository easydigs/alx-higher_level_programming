#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    lo = 0
    hi = len(list_of_integers)

    while lo < hi:
        mid = (lo + hi) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) \
                and (mid == hi - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            hi = mid
        else:
            lo = mid + 1

    return None
