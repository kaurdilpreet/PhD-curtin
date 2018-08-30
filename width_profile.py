#!/usr/bin/env python

import numpy as np
from scipy.integrate import simps
from numpy import trapz
from numpy import genfromtxt
import matplotlib.pyplot as plt
from matplotlib.pyplot import xticks
from matplotlib.ticker import MultipleLocator

my_data = genfromtxt('ascii_123-124.csv', delimiter=',')
x = my_data.T[2]
y = my_data.T[3]

new_y = np.concatenate((y, y))
x_more =  np.arange(256, 256 * 2)
new_x = np.concatenate((x, x_more))

plt.plot(new_x, new_y)
plt.savefig('123.png')

a = new_x[100:355]
#print a
b = new_y[100:355]
#print b

# get rms
flux_rms = b[a < 200]
#rms = np.sqrt(np.mean(np.square(flux_rms)))
#print(rms)
stdev = np.std(b[a < 200])
print(stdev)

a_on = a[b > 3 * stdev]
print('bin number for on is', len(a_on))
a_on2 = a[b > 3* stdev]
print('ON bin no with stdev is', len(a_on2))

area = simps(b[b > 3 * stdev], dx=1)
print("area =", area)

ratio = area / max(b)

print('width in terms of bins', ratio)
print('width in terms of ms (Period/width)', ratio*(2.18/256))

plt.plot(a,b)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
spacing = 5 # This can be your user specified spacing.
minorLocator = MultipleLocator(spacing)
ax1.plot(a,b)

# Set minor tick locations.
ax1.xaxis.set_minor_locator(minorLocator)

# Set grid to use minor tick locations.
ax1.grid(which = 'minor')
ax1.hlines(y=3*stdev, xmin=100, xmax=356, linewidth=1, color='r')
plt.savefig('profile_123-124.png')

