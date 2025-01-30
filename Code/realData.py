import numpy as np
from continuedFractions import getData
from matplotlib import pyplot as plt
"""
The goal here is to see the frequency of each integer in a
random sample of real continued fractions
"""
size = 4
terms = []
freqs = []
arrs = []
nums = []
for i in range(size):
    r = np.float64(np.random.rand())
    a, b, arr, std = getData(r, 1000)
    terms.append(a.keys())
    freqs.append(a.values())
    arrs.append(arr)
    print([b, std])
    nums.append(r)


fig = plt.figure()
plt0bar = fig.add_subplot(421)
plt4bar = fig.add_subplot(423)
plt2bar = fig.add_subplot(425)
plt_1bar = fig.add_subplot(427)

plt0box = fig.add_subplot(422)
plt4box = fig.add_subplot(424)
plt2box = fig.add_subplot(426)
plt_1box = fig.add_subplot(428)

plt0bar.set_title(nums[0], loc='center', pad=1)
plt4bar.set_title(nums[int(size/4)], loc='center', pad=1)
plt2bar.set_title(nums[int(size/2)], loc='center', pad=1)
plt_1bar.set_title(nums[-1], loc='center', pad=1)

plt0bar.bar(terms[0], freqs[0])
plt4bar.bar(terms[int(size/4)], freqs[int(size/4)])
plt2bar.bar(terms[int(size/2)], freqs[int(size/2)])
plt_1bar.bar(terms[-1], freqs[-1])

plt0box.boxplot(arrs[0], vert=False)
plt4box.boxplot(arrs[int(size/4)], vert=False)
plt2box.boxplot(arrs[int(size/2)], vert=False)
plt_1box.boxplot(arrs[-1], vert=False)


plt.show()