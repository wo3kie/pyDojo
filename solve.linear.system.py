#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./python solve.linear.system.py
#

import numpy as np
import scipy as sp
import scipy.linalg as spla

#
#  x     + 2z = 5
# 2x - y + 3z = 7
# 4x + y + 8z = 10
#

A = np.array([
	[ 1,  0, 2],
	[ 2, -1, 3],
	[ 4,  1, 8]
])

#
# Inverse
#

ADet = np.linalg.det(A)
assert(ADet != 0.0)

AInverse = np.linalg.inv(A)

actual = AInverse
expected = np.array([
	[-11,  2,  2],
    [ -4, -0,  1],
    [  6, -1, -1]
])

assert((actual == expected).all())
assert(np.array_equal(actual, expected))

b = np.array([
	5,
	7,
	10
])

#
# solve
#

x = np.linalg.solve(A, b)

actual = x
expected = np.array([
	-21,
	-10,
	13
])

assert((actual == expected).all())
assert(np.array_equal(actual, expected))

#
# PA = LU
#

P, L, U = spla.lu(A)

actual = P
expected = np.array([
	[ 0, 0, 1],
	[ 0, 1, 0],
	[ 1, 0, 0]
])

assert((actual == expected).all())
assert(np.array_equal(actual, expected))

actual = L
expected = np.array([
	[ 1,    0,     0 ],
	[ 0.5,  1,     0 ],
	[ 0.25, 0.167, 1 ]
])

assert(np.allclose(actual, expected, rtol=0.1))

actual = U
expected = np.array([
	[ 4,  1,    8     ],
	[ 0, -1.5, -1     ],
	[ 0,  0,    0.167 ]
])

assert(np.allclose(actual, expected, rtol=0.1))

