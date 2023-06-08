#!/usr/bin/python3
import dis
import hidden_4
if __name__ == "__main__":
    names = [name for name in dir(hidden_4)]
    sorted_names = sorted(names)
    for name in sorted_names:
        if not name.startswith('__'):
            print(name)
