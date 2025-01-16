import numpy as np

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

x = np.sqrt(7)+3j*np.pi
print(aHurwitz(x, 100))
    