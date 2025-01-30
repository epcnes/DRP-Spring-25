import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from random import random as rand
from random import randint
''' contfrac(r, n) -> list
As seen in Kopparty, pg. 1:
take any r in the reals, then
r = floor(r) + 1/r_1
r_(n-1) = floor(r_(n-1)) + 1/r_n
etc.
@param r real number to approximate
@param n max number of terms to calculate
@returns arr the list form of the simple continued fraction of r
'''
def contFrac(r, n: int):
    arr = []
    for _ in range(n+1):
        a = int(r)
        arr.append(a)
        if r-a == 0:
            break
        r = 1 / (r-a)
    return arr

''' getData(r) -> list
here "arr" means the simple continued fraction of r in list form
returns statistical information about arr 

@params r real number to approximate

@returns rX the list of unique denominators
@returns rY the frequency of denominators
@returns mean the mean of the elements in arr
'''
def getData(r, n):
    rArr = contFrac(r, n)
    rDict = dict(Counter(rArr))

    mean = np.float64(np.mean(rArr))
    std = np.float64(np.std(rArr))

    return rDict, mean, rArr, std
    # print(f"Unique terms: {rX} \nMean of all terms: {mean} \nStandard Deviation: {std} \nUpper outlier: {outlierQ3} \nLower outlier: {outlierQ1} \nMax of terms: {np.max(rX)}")
    # plt.boxplot(rX)
    # plt.show()
    # return [rX, rY, mean, std, outlierQ3, outlierQ1, np.max(rX)] #

''' compContFrac(x) -> float
calculates the value of a given simple continued fraction in list form

@params x list form of a real number

@returns approximation of a real number
'''
def compContFrac(x : list):
    sum = 0
    for c in reversed(x):
        if sum == 0:
            sum = c
        else:
            sum = c + 1 / sum
    return sum