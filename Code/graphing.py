from complexContinuedFractions import getData
import numpy as np
from matplotlib import pyplot as plt
"""
Graphing terms of a complex continued fraction
"""

# z = random()*randint(-1000, 1000) + random()*randint(-1000, 1000)*1j
z = np.sqrt(1/np.random.rand()) + 1/np.random.rand()*1j

x, y, zDict = getData(z)
fig = plt.figure()
ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122)
ax0.scatter(x,y)
ax0.set_title("Scatter")
ax1.bar(zDict.keys(), zDict.values())
ax1.set_title("Bar")
fig.suptitle(z)

plt.show()