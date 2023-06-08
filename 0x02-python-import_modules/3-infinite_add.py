#!/usr/bin/python3
import sys
if __name__ == '__main__':
    a = sys.argv
    count = 0
    z = len(a)
    for i in range(1, z, 1):
        count += int(a[i])
    print(count)
