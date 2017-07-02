#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./assert
#

import inspect

USE_ASSERT = True

def ShrinkString(text, width):
    if len(text) <= width:
        return text

    return text[0:width-3] + "..."

def Assert(actual, expected, message="", eps=0.0001):
    if USE_ASSERT == False:
        return

    if type(actual) == float and type(expected) == float:
        if(abs(actual - expected) < eps):
            return

    if(actual == expected):
        return

    print("\nAssert failed, actual `{0}' is not equal to expected `{1}'". \
        format(actual, expected, message))

    stack = inspect.stack()

    max_filename_length = max([len(frame.filename) for frame in stack])
    max_filename_length = min(20, max_filename_length)
    max_function_length = max([len(frame.function) for frame in stack])
    max_function_length = min(20, max_function_length)

    for frame in stack[1:]:
        format = "{0: <" + str(max_filename_length) + "}:" \
            + "{1: >5}\t" \
            + "{2: <" + str(max_function_length) + "}\t" \
            + "`{3}'"

        print(format.format(
            ShrinkString(frame.filename, max_filename_length),
            frame.lineno,
            ShrinkString(frame.function, max_function_length),
            ShrinkString(frame.code_context[0].strip(), 40)
        ))

        # exit(1)

def ShrinkString_test():
    Assert(ShrinkString("a", 5), "a")
    Assert(ShrinkString("ab", 5), "ab")
    Assert(ShrinkString("abc", 5), "abc")
    Assert(ShrinkString("abcd", 5), "abcd")
    Assert(ShrinkString("abcde", 5), "abcde")
    Assert(ShrinkString("abcdef", 5), "ab...")
    Assert(ShrinkString("abcdefg", 6), "abc...")

def VeryVeryVeryVeryVeryVeryLongFunctionName():
    Assert(1, 2)

def Assert_test():
    Assert(1.1, 1.2, "")

    VeryVeryVeryVeryVeryVeryLongFunctionName()

def main():
    ShrinkString_test()
    Assert_test()

main()

