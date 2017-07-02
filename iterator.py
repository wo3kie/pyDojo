#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./iterator.py
#

class Fibonacci:
    def __init__(self):
        self.prev_prev = 0
        self.prev = 1

    def __iter__(self):
        return self

    def __next__(self):
        current = self.prev_prev + self.prev

        self.prev_prev = self.prev
        self.prev = current

        return current


def main():
    for i in Fibonacci():
        print(i)

        if i > 100:
            break

main()

