#!user/bin/env/python

import numpy as np
import matplotlib.pyplot as plt

file = '/Users/dilpreetkaur/Dropbox/DM.csv'
data = np.genfromtxt(file, delimiter=',')
#print(data.shape)

plt.plot(data[:,1], data[:,2], '-b*', label='DM across frequency')
plt.xlabel('Frequency')
plt.ylabel('DM')
plt.title('Year 2016')
plt.legend()
plt.show()
