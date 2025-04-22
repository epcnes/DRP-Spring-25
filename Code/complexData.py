from complexContinuedFractions import getData, N
import numpy as np
from matplotlib import pyplot as plt
"""
Graphing terms of a complex continued fraction
"""
for i in range(2):
    z = np.random.rand()*10 + np.random.rand()*1j

    x, y, zDict, c = getData(z)
    fig = plt.figure()
    ax0 = fig.add_subplot(121)
    ax1 = fig.add_subplot(122)

    ax0.scatter(x,y)
    ax0.set_xlabel("Re(x)")
    ax0.set_ylabel("Im(x)")
    ax0.set_title("Plotting Complex Partial Denominatos")

    keyNorms = []
    for i in zDict:
        keyNorms.append(N(i))
    ax1.bar(keyNorms, zDict.values())
    ax1.set_title("Norms of Complex Partial Denominators")
    ax1.set_xlim(0, max(keyNorms))
    ax1.set_ylim(0, max(zDict.values()))
    fig.suptitle(z)

    print(np.mean(c))
    plt.get_current_fig_manager().resize(1800, 1000)
    plt.show()