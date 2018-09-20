#!/usr/bin/env python

import numpy as np
from numpy.linalg import lstsq
from numpy import genfromtxt 
from numpy import math
from scipy import optimize

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab

my_data = genfromtxt('WA_flux_allobs.csv', delimiter=',')
x = my_data.T[0]
y = my_data.T[1]
z = my_data.T[2]

x1 = my_data.T[0][:12]
y1 = my_data.T[1][:12]
z1 = my_data.T[2][:12]

logx1 = np.log10(x1)
logy1 = np.log10(y1)
logz1 = np.log10(z1)

x2 = my_data.T[0][12:]
y2 = my_data.T[1][12:]
z2 = my_data.T[2][12:]

logx2 = np.log10(x2)
logy2 = np.log10(y2)
logz2 = np.log10(z2)


def test_func1(logx1, a1, b1):
    return a1*logx1 + b1

params1, params_covariance1 = optimize.curve_fit(test_func1, logx1, logy1, p0=[2,2])
print(params1)
print(params_covariance1)
perr1 = np.sqrt(np.diag(params_covariance1))
print perr1

def test_func2(logx2, a2, b2):
    return a2*logx2 + b2

params2, params_covariance2 = optimize.curve_fit(test_func2, logx2, logy2, p0=[2,2])
print(params2)
print(params_covariance2)
perr2 = np.sqrt(np.diag(params_covariance2))
print perr2



plt.errorbar(x, y, yerr=z, fmt='.', ecolor='orangered', label='J2241-5236 MWA+PKS',color='steelblue', capsize=2,  markersize=3)
plt.yscale('log')
plt.xscale('log')
#label values are read from terminal output
plt.plot(x1, 10**(test_func1(logx1, params1[0], params1[1])), 'k', linestyle='--', label='MWA=-1.85$\pm$0.36')
plt.plot(x2, 10**(test_func2(logx2, params2[0], params2[1])), 'r', linestyle='--', label='PKS=-2.42$\pm$0.17') 

#plt.plot(x, 10**)m*logx + c), 'r', linestyle='--') 

plt.legend()
plt.xlabel("Frequency (MHz)")
plt.ylabel("Flux density (mJy)")
plt.savefig('2fit_allobs_flux_plot.png')


