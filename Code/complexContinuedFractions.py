import numpy as np
from collections import Counter

'''aHurwitz(x) -> list'''
# |  This method implements Algorithm 4.7 presented in 
# |  Cijsouw, pg 38, created in 1887 by Adolf Hurwitx
# |  
# |  @params x complex number
# |  @params n max number of terms
# |  
# |  @returns list form of the complex continued fraction of x
def aHurwitz(x : complex, n : int):
    c = []
    for _ in range(n):
        a = int(np.round(np.real(x))) + int(np.round(np.imag(x)))*1j # gives Gaussian Integer
        c.append(a)
        if x == a:
            break
        x = 1/(x - a)
    return c
    
def getData(c : iter):
    n = 1000
    z = aHurwitz(c, n)
    x, y = ([c.real for c in z], [c.imag for c in z])
    zDict = dict(Counter(z))

    xMean = np.mean(x)
    yMean = np.mean(y)
    xSTD = np.std(x)
    ySTD = np.std(y)

    # print(f"Term Counter: {zDict}\nx mean: {xMean}\nsd: {xSTD}\ny mean: {yMean}\nsd: {ySTD}")
    return x, y, zDict