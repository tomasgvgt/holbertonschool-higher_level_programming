#!/usr/bin/python3
for d in range(10):
    for u in range(10):
        if d < u:
            if d == 8 and u == 9:
                print("{}{}".format(d, u))
            else:
                print("{}{}".format(d, u), end=", ")
