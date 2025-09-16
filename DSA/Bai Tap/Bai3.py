import numpy as np

ar_1 = np.arange(0,11,1)

ar_2 = np.arange(1,10)
ar_2 = ar_2.reshape(3,3)

print(ar_1)
print(ar_2)
print(ar_2[1][0])