import numpy as np
from continuedFractions import getData
from matplotlib import pyplot as plt
"""
The goal here is to see the frequency of each integer in a
random sample of real continued fractions
"""
size = 1000
terms = []
freqs = []
arrs = []
means = []
for i in range(size):
    #r = np.float64(np.sqrt(1/np.random.rand()))
    r = np.float64(np.random.rand())
    a, b = getData(r)
    terms.append(a.keys())
    freqs.append(a.values())
    means.append(b)


fig = plt.figure()
plt0bar = fig.add_subplot(421)
plt99bar = fig.add_subplot(423)
plt499bar = fig.add_subplot(425)
plt999bar = fig.add_subplot(427)

plt0box = fig.add_subplot(422)
plt99box = fig.add_subplot(424)
plt499box = fig.add_subplot(426)
plt999box = fig.add_subplot(428)

plt0bar.set_title(means[0], loc='center', pad=0.5)
plt99bar.set_title(means[int(size/4)], loc='center', pad=0.5)
plt499bar.set_title(means[int(size/2)], loc='center', pad=0.5)
plt999bar.set_title(means[-1], loc='center', pad=0.5)

plt0bar.hist(a[0])
plt99bar.hist(a)
plt499bar.hist(a)
plt999bar.hist(a)

plt.show()