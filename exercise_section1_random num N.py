import numpy as np
from numpy.random import randn
randn()
#arithmetic logical exp logical operators loop
"""
N = 10
counter = 0
for i in randn(N):
    if (i > -1 and i < 1):
        counter = counter + 1
ans = counter / N
print(ans)
"""
N = 10
counter = 0
for i in randn(N):
    if -2 < i > -1 and 1 < i > 2:
        counter = counter+1
ans = counter / N
print(randn(N))
print(ans)
