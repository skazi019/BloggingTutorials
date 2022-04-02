import os
import sys

print([x for x in sys.path])

import module1
# import ..dir2.module2

[print(x) for x in sys.path]

print(module1.a)
module1.basic_func()

# print(module2.a)
