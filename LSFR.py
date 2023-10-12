import numpy as np
from pylfsr import LFSR


state = [1,0,0,1,1,0,0,0,0,1]
fpoly = [10,3]
L=LFSR(fpoly=fpoly,initstate =state)
L.info()
tempseq = L.runKCycle(10000)
print(L.arr2str(tempseq))
