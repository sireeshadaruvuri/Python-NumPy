import numpy as np
#arithmentic operations on arrays can be smoothly performed if they have same shape and dimensions
a = np.array([[1,2,3],[3,4,5]])
b = np.array([[2,3,6],[5,6,7]])
c = a*b
print('values in c are', +c)
#If the dimensions of two arrays are dissimilar, element-to-element operations are not possible.
# However, operations on arrays of non-similar shapes is still possible in NumPy,
# because of the broadcasting capability. The smaller array is broadcast to the size of the larger array
# so that they have compatible shapes.
a = np.array([[1,2,3],[2,3,4]])
b = np.array([2,2,2])
c = a+b
print('new broadcasting values in c are', +c)
