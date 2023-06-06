#!/usr/bin/python3
for w in range(0, 10, 1):
    for v in range(0, 10):
        if w != v and w < v:
            print("{}{}".format(w, v), end='\n' if w == 8 and v == 9 else ', ')
