#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    j = ()
    for i in (tuple_a, tuple_b):
        if len(i) == 0:
            i = (0, 0)
        elif len(i) == 1:
            i = (i[0], 0)
        if j == ():
            j = i
    return (i[0] + j[0], i[1] + j[1])
