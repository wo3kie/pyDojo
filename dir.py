#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./dir.py
#

class Class:
    def __init__(self, x):
        self.x = x


    def get(self):
        return self.x


    def set(self, x):
        self.x = x


    def __str__(self):
        return str(self.x)


    @staticmethod
    def static():
        return 0


dict = Class.__dict__

assert '__init__' in dict
assert 'get' in dict
assert 'set' in dict
assert '__str__' in dict
assert 'unknown' not in dict

cls = Class(42)

assert str(cls) == "42"

type(cls).__dict__['set'].__get__(cls, cls.__class__)(24)
type(cls).__dict__['set'].__get__(cls, type(cls))(24)
type(cls).__dict__['set'].__get__(cls, Class)(24)

assert type(cls).__dict__['get'].__get__(cls, cls.__class__)() == 24
assert type(cls).__dict__['get'].__get__(cls, type(cls))() == 24
assert type(cls).__dict__['get'].__get__(cls, Class)() == 24

assert type(cls).__dict__['static'].__get__(None, cls.__class__)() == 0
assert type(cls).__dict__['static'].__get__(None, type(cls))() == 0
assert type(cls).__dict__['static'].__get__(None, Class)() == 0


