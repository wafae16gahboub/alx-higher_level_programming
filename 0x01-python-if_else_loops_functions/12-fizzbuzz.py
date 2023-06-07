#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100, 1):
        y = i // 3
        x = (y * 3) - i
        v = i // 5
        if x == 0 and ((v * 5) - i) == 0:
            print("FizzBuzz", end=" ")
        elif x == 0:
            print("Fizz", end=" ")
        elif ((v * 5) - i) == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=(" "))
