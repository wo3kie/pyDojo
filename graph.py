#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./python graph.py
#

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**2 + 5*x - 10

_, sp = plt.subplots()
sp.plot(x, y, color="blue", label="y(x**2 + 5*x - 10)")

sp.set_xlabel("x")
sp.set_ylabel("y")

sp.legend()

sp.grid(color="grey", which="major", linestyle=":", linewidth=1)

plt.show()

