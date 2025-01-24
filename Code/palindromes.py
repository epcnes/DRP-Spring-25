import numpy as np
from random import randint as rand
from continuedFractions import compContFrac

n = 10
an = []
for i in range(n):
    an.append(rand(-100, 100))
bn = an[::-1]
cn = an+bn
      
    
print(cn, compContFrac(cn))