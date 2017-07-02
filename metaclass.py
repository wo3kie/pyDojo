#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./metaclass.py
#

def init(self, x):
    self.x = x

def to_string(self):
    return str(self.x)

Class = type(
    "Class",
    (object,),
    {
        "__init__" : init,
        "__str__" : to_string
    }
)

cls = Class(42)
print(str(cls))

