import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
from random import random as rand
'''contfrac(r, n) -> list'''
# |  as seen in Kopparty, pg. 1:
# |  take any r in the reals, then
# |  r = floor(r) + 1/r_1
# |  r_(n-1) = floor(r_(n-1)) + 1/r_n
# |  etc.
# | 
# |  @param r real number to approximate
# |  @param n number of terms to calculate
# |
# |  @returns arr the list form of the simple continued fraction of r
def contFrac(r, n: int):
    arr = []
    for _ in range(n):
        a = int(r)
        arr.append(a)
        if r-a == 0:
            break
        r = 1 / (r-a)
    return arr

'''getData(r) -> list'''
# |  here "arr" means the simple continued fraction of r in list form
# | 
# |  returns statistical information about arr 
# |  
# |  @params r real number to approximate
# |  
# |  @returns rX the list of unique denominators
# |  @returns rY the frequency of denominators
# |  @returns mean the mean of the elements in arr
# |  @returns std the standard deviation of elements in arr
# |  @returns outlier calculated as Q3 + 1.5*std
def getData(r):
    n = 1000
    rArr = contFrac(r, n)
    rDict = dict(Counter(rArr))
    rX, rY = (list(rDict.keys()), list(rDict.values()))

    mean = np.float64(np.mean(r))
    std = np.float64(np.std(r))
    outlierQ3 = np.quantile(r, .75) + (1.5*std)
    outlierQ1 = np.quantile(r, .25) + (1.5*std)

    print(rX, rY, mean, std, outlierQ3, outlierQ1, np.max(rX), np.equal(mean, r))
    plt.boxplot(rX)
    plt.show()
    # return [rX, rY, mean, std, outlierQ3, outlierQ1, np.max(rX)] #

r = np.float64(np.sqrt(rand()))
print(r)
getData(r)