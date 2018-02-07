#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
from numpy import trapz
import scipy.integrate as integrate


file = '/Users/dilpreetkaur/Dropbox/allprofiles_147-148.csv'
phase, amp = np.genfromtxt(file, delimiter=',', unpack=True)
#print(data.shape)

plt.plot(phase, amp, '-b*', label='Pulse profile')
plt.xlabel('Phase')
plt.ylabel('Flux')
plt.title('Frequency 147-148')
plt.legend()
plt.show()

y = amp
interval = 10
area = trapz(y, dx=11000)
#area = integrate(y,interval)
print (area)
