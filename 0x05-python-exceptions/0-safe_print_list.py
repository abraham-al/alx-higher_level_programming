#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            print('{}'.format(my_list[i]), end='')
            a += 1
        except:
            pass
    print()
    return a
