import numpy as np
from continuedFractions import getData
from matplotlib import pyplot as plt
"""
The goal here is to see the frequency of each integer in a
random sample of continued fractions
"""
size = 2000
terms = []
freqs = []
means = []
for i in range(size):
    #r = np.float64(np.sqrt(1/np.random.rand()))
    r = np.float64(np.random.rand())
    a, b = getData(r)
    terms.append(a.keys())
    freqs.append(a.values())
    means.append(b)


fig = plt.figure()
plt0 = fig.add_subplot(141)
plt99 = fig.add_subplot(142)
plt499 = fig.add_subplot(143)
plt999 = fig.add_subplot(144)

plt0.set_title(means[0], loc='center', pad=0.5)
plt99.set_title(means[int(size/4)], loc='center', pad=0.5)
plt499.set_title(means[int(size/2)], loc='center', pad=0.5)
plt999.set_title(means[-1], loc='center', pad=0.5)

plt0.bar(terms[0], freqs[0])
plt99.bar(terms[int(size/4)], freqs[int(size/4)])
plt499.bar(terms[int(size/2)], freqs[int(size/2)])
plt999.bar(terms[-1], freqs[-1])

plt.show()