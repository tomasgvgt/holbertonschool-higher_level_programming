#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i = 0 in range(x):
        try:
            print(my_list[i], end="")
            i++
        except Indexerror:
            break
        print()
        return i
