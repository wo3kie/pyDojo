#!/usr/bin/env python3

#
# Website:
#     https://github.com/wo3kie/pyDojo
#
# Author:
#     Lukasz Czerwinski
#
# Usage:
#     $ ./dir_walk.py ./dir_walk.py
#     ./dir_walk.py
#
#     $ ./dir_walk.py .
#     ./static_method.py
#     ./solve_linear_system.py
#     ./generator.py
#     ./decorator.py
#     ./plot.py
#     ./dir_walk.py
#     ...
#

import os
import sys

if os.path.isfile(sys.argv[1]):
    print(sys.argv[1])
elif os.path.isdir(sys.argv[1]):
    for dir_name, sub_dir_list, file_list in os.walk(sys.argv[1]):
        for file in file_list:
            if file.endswith(".py"):
                print(os.path.join(dir_name, file))
else:
    print("Neither file nor directory %s" % sys.argv[1])

