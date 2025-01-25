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
    r = np.float64(np.sqrt(1/np.random.rand()))
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

plt0bar.set_ylim(ymax = max(freqs[0]))
plt99bar.set_ylim(ymax = max(freqs[99]))
plt499bar.set_ylim(ymax = max(freqs[499]))
plt999bar.set_ylim(ymax = max(freqs[999]))

plt0bar.bar(terms[0], freqs[0])
plt99bar.bar(terms[int(size/4)], freqs[int(size/4)])
plt499bar.bar(terms[int(size/2)], freqs[int(size/2)])
plt999bar.bar(terms[-1], freqs[-1])

plt0bar.bar(terms[0], freqs[0])
plt99bar.bar(terms[int(size/4)], freqs[int(size/4)])
plt499bar.bar(terms[int(size/2)], freqs[int(size/2)])
plt999bar.bar(terms[-1], freqs[-1])

plt.show()