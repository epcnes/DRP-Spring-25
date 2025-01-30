import numpy as np
from continuedFractions import getData
from matplotlib import pyplot as plt
"""
The goal here is to see the frequency of each integer in a
random sample of real continued fractions
"""
size = 100
terms = []
freqs = []
arrs = []
means = []
for i in range(size):
    #r = np.float64(np.sqrt(1/np.random.rand()))
    r = np.float64(np.random.rand())
    a, b, arr = getData(r)
    terms.append(a.keys())
    freqs.append(a.values())
    arrs.append(arr)
    means.append(b)


fig = plt.figure()
plt0bar = fig.add_subplot(421)
plt4bar = fig.add_subplot(423)
plt2bar = fig.add_subplot(425)
plt_1bar = fig.add_subplot(427)

plt0box = fig.add_subplot(422)
plt4box = fig.add_subplot(424)
plt2box = fig.add_subplot(426)
plt_1box = fig.add_subplot(428)

plt0bar.set_title(means[0], loc='center', pad=0.5)
plt4bar.set_title(means[int(size/4)], loc='center', pad=0.5)
plt2bar.set_title(means[int(size/2)], loc='center', pad=0.5)
plt_1bar.set_title(means[-1], loc='center', pad=0.5)

plt0bar.bar(terms[0], freqs[0])
plt4bar.bar(terms[int(size/4)], freqs[int(size/4)])
plt2bar.bar(terms[int(size/2)], freqs[int(size/2)])
plt_1bar.bar(terms[-1], freqs[-1])

plt0box.boxplot(arrs[0])
plt4box.boxplot(arrs[int(size/4)])
plt2box.boxplot(arrs[int(size/2)])
plt_1box.boxplot(arrs[-1])


plt.show()