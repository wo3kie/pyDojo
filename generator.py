#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./generator.py
#

def fibonacci():
    yield 1
    yield 1

    prev_prev = 1
    prev = 1
    current = prev_prev + prev

    while current < 50:
        yield current

        prev_prev = prev
        prev = current
        current = prev_prev + prev


def Enumerate(xs):
    counter = 0

    for x in xs:
        yield (counter, x)
        counter += 1


def Zip(xs, ys):
    assert len(xs) == len(ys)

    for i in range(len(xs)):
        yield xs[i], ys[i]


def main():
    for f in fibonacci():
        print(f)

    for id, value in Enumerate("python"):
        print("%d %s" % (id, value))

    for x, y in Zip("python", "erlang"):
        print("%s %s" % (x, y))


main()

