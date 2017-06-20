#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./static_method.py
#

class StaticMethod:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        return self.f(*args)


def static_method(f):
    return StaticMethod(f)


def hImpl(*args):
    return 1


class Test:
    def e():
        return 0

    e = StaticMethod(e)

    @static_method
    def f():
        return 3.14

    def g():
        return 2.71

    g = static_method(g)

    h = hImpl

def main():
    assert Test.e() == 0
    assert Test().e() == 0

    assert Test.f() == 3.14
    assert Test().f() == 3.14

    assert Test.g() == 2.71
    assert Test().g() == 2.71

    assert Test.h() == 1
    assert Test().h() == 1

main()

