import matplotlib.pyplot as plt
import numpy as np

# read the wise cata
csv_data = '/Users/dilpreetkaur/Dropbox/DM.csv'
DM_csv_open = open(csv_data, 'r').readlines()
n = len(DM_csv_open)

x = []
y = []
z = []
filter = []

for i in range(2, n - 2):
    line_split = DM_csv_open[i].split(',')
    filter.append(line_split[0])
    x.append(float(line_split[1]))
    y.append(float(line_split[2]))
    z.append(float(line_split[3]))

x = np.asarray(x)
y = np.asarray(y)
z = np.asarray(z)

filter_use = filter[filter != '#']
print(filter_use)
# x = x(filter_use)
print(x)

# plt.errorbar(x, y, yerr=z, fmt='b*')
# plt.show()
# plt.savefig('~/Dropbox/test.png')
