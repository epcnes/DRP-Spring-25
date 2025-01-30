from complexContinuedFractions import getData, N
import numpy as np
from matplotlib import pyplot as plt
"""
Graphing terms of a complex continued fraction
"""
for i in range(5):
    z = np.random.rand()*10 + np.random.rand()*1j

    x, y, zDict, c = getData(z)
    fig = plt.figure()
    ax0 = fig.add_subplot(121)
    ax1 = fig.add_subplot(122)
    ax0.scatter(x,y)
    ax0.set_title("Scatter")

    keyNorms = []
    for i in zDict:
        keyNorms.append(N(i))
    ax1.bar(keyNorms, zDict.values())
    ax1.set_title("Bar")
    ax1.set_xlim(0, max(keyNorms))
    ax1.set_ylim(0, max(zDict.values()))
    fig.suptitle(z)

    print(np.mean(c))

    plt.show()