#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(0,x):
        try:
            print(f"{my_list[i]}", end="")
            j += 1
        except IndexError:
            continue
    print()
    return (j)
