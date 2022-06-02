#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        stat = add(a, b)
        for i in range(4, 6):
            stat = add(stat, i)
        return (stat)
    else:
        return (sub(a, b))
