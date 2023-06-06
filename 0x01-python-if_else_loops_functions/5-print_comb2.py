#!/usr/bin/python3
for w in range(0, 100):
    if w == 99:
        print("{}".format(w))
    else:
        print("{:02}".format(w), end=", ")
