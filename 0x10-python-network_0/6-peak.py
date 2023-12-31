#!/usr/bin/python3
"""
Defines an algorithm for finding the peak of an unsorted list of integers
"""


def find_peak(list_of_integers):
    """
        Find a peak in a list of unsorted integers.

        Args:
            list_of_integers (list): List of unsorted integers.

        Returns:
            The peak element.
    """
    if list_of_integers == []:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
