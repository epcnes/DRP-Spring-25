import numpy as np
from collections import Counter

''' aHurwitz(x) -> list
This method implements Algorithm 4.7 presented in 
Cijsouw, pg 38, created in 1887 by Adolf Hurwitx

@params x complex number
@params n max number of terms

@returns list form of the complex continued fraction of x
'''
def aHurwitz(x : complex, n : int):
    c = []
    for _ in range(n):
        a = int(np.round(np.real(x))) + int(np.round(np.imag(x)))*1j # gives Gaussian Integer
        c.append(a)
        if x == a:
            break
        x = 1/(x - a)
    return c
''' getData(c) -> list, list, dict
This method takes the result of aHurwitz and returns the real and imaginary parts
of each term and a tally of each unique term in the form of a dictionary

@params c list form of complex continued fraction

@returns x real part of each partial quotient
@returns y imaginary part of each partial quotient
@returns zDict dictionary of unique terms and their frequencies
'''
def getData(c : iter):
    n = 1000
    z = aHurwitz(c, n)
    x, y = ([c.real for c in z], [c.imag for c in z])
    zDict = dict(Counter(z))

    xMean = np.mean(x)
    yMean = np.mean(y)
    xSTD = np.std(x)
    ySTD = np.std(y)

    return x, y, zDict