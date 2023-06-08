#!/usr/bin/python3
import sys
if __name__ == '__main__':
    x = sys.argv
    y = len(x) - 1
    if y == 0:
        print("{} arguments.".format(y))
    elif y == 1:
        print("{} argument:".format(y))
        print("{}: {}".format(y, x[1]))
    else:
        print("{} arguments:".format(y))
        for i in range(1, len(y)):
            print("{}: {}".format(i, x[n]))
