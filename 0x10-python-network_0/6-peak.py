#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """function to find the peak"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
