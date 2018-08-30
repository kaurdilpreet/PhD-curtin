#!/usr/bin/env python

import numpy as np
from numpy.linalg import lstsq
from numpy import genfromtxt 
from numpy import math

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

my_data = genfromtxt('flux_plot.csv', delimiter=',')
x = my_data.T[0]
y = my_data.T[1]
z = my_data.T[2]

logx = np.log10(x)
logy = np.log10(y)
logz = np.log10(z)

A = np.vstack([logx, np.ones(len(logx))]).T
print A

m,c = np.linalg.lstsq(A, logy, rcond=None)[0]
print(m,c)


plt.errorbar(x, y, yerr=z, fmt='.', ecolor='orangered', label='J2241-5236 MWA+PKS',
            color='steelblue', capsize=0.1)
plt.yscale('log')
plt.xscale('log')
plt.plot(x, 10**(m*logx + c), 'r', linestyle='--') 
plt.legend()
plt.xlabel("Frequency (MHz)")
plt.ylabel("Flux density (mJy)")
plt.savefig('flux_plot.png')

