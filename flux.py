#!/usr/bin/env python

import numpy as np
import csv
import math
import uncertainties
from uncertainties import ufloat
from uncertainties import umath

x  = []
y  = []
z  = []
a  = []
b  = []
c  = []


with open('/Users/dilpreetkaur/Dropbox/beam_sim_13aug17.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[1]))
        y.append(float(row[2]))
        z.append(float(row[3]))
	a.append(float(row[4]))
	b.append(float(row[5]))
	c.append(float(row[6]))

SEFD = np.array(c) * np.array(z) / np.array(y)
print SEFD
S = np.array(a) * (np.array(c) * np.array(z)) / (np.array(y) * math.sqrt(2*1.28*3600))
print S
Rms = ((SEFD) / math.sqrt(2*1280000*3600)) * 1000
print Rms

res = [SEFD],[S],[Rms]
csvfile = "/Users/dilpreetkaur/Dropbox/output.csv"

with open(csvfile, 'w') as output:
    writer = csv.writer(output,lineterminator='\n')
    writer.writerows(res)


#alpha = np.array(uncertainties.umath (log(S)))
#print alpha


#X = sp.symbols('')
#F = sp.Function('')(X)

#weighted_avg = np.average(y, weights=z)
#e = np.power(z,2)
#weighted_err = sum(1/e)
#print error
#print weighted_avg
#print(math.sqrt(1/(weighted_err)))
