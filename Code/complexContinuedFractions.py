import numpy as np

'''aHurwitz(z) -> list'''
# |  This method implements Algorithm 4.7 presented in 
# |  Cijsouw, pg 38, created in 1887 by Adolf Hurwitz
# |  
# |  @params z complex number
# |  @params n max number of terms
# |  
# |  @returns list form of the complex continued fraction of z
def aHurwitz(z : complex, n : int):
    c = []
    for i in range(n):
        c.append(z)
        a = np.fix(np.real(z)+0.5); b = np.fix(np.imag(z)+0.5) # Definition 4.1 (Cijsouw, pg. 38)
        flAH = a + complex(0,b) # complex() is used to preserve b as the imaginary part of z
        # sgAH: C -> {-1, 1, -i, i} which can be achieved by np.sign()
        if z-flAH == 0:
            break
        z = np.sign(z)/(z - flAH)
        
    np.set_printoptions(suppress=True)
    print(c, len(c))

z = complex(np.sqrt(7), 3*np.pi)
print(z)
aHurwitz(z, 10)
    