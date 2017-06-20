#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./decorator.py
#

def decorator(f):
    print("From decorator")

    def wrapper(*args):
        return f(*args)

    return wrapper


@decorator
def add(x1, x2):
    return x1 + x2


def mul(x1, x2):
    return x1 * x2

mul = decorator(mul)

def main():
    assert add(1, 2) == 3
    assert mul(1, 2) == 2

main()

