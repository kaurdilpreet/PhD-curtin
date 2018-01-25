#! user/bin/env/python

import sys

DM = float(sys.argv[1])
f1 = float(sys.argv[2])
f2 = f1 + 0.01
t = 4.148808e6 * ((f1**-2) - (f2**-2)) * DM
print(t)
