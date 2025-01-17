import numpy as np
from continuedFractions import getData

"""
The goal here is to see the frequency of each integer in a
random sample of continued fractions
"""
size = 1000
terms = []
freqs = []
means = []
for i in range(size):
    r = np.float64(np.sqrt(1/np.random.rand()))
    a, b = getData(r)
    terms.append(a.keys())
    freqs.append(a.values())
    means.append(b)

print(terms)