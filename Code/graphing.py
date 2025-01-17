from complexContinuedFractions import aHurwitz, getData
import numpy as np
from matplotlib import pyplot as plt
"""
Graphing terms of a continued fraction of a complex number
"""

# z = random()*randint(-1000, 1000) + random()*randint(-1000, 1000)*1j
z = np.sqrt(1/np.random.rand()) + 1/np.random.rand()*1j

x, y = getData(z)
plt.scatter(x,y)
print(z)
plt.show()