import numpy as np
a = np.arange(0,60,5)
a = a.reshape(4,3)
print(a)
for x in np.nditer(a):
    print(x)
b = a.T #transpose matrix(rows n columns r reversed)
print(b)
for y in np.nditer(b):
    print(y)
#If the same elements are stored using F-style order,
# the iterator chooses the more efficient way of iterating over an array.
c = b.copy(order = 'c')
print(c)
for x in np.nditer(c):
    print('values in x are', +x)
d = b.copy(order = 'f')
print('values in d with f are', +d)
for y in np.nditer(d):
    print('values in y with f are',+y)
#It is possible to force nditer object to use a specific order by explicitly mentioning it.
#another way to do above with order f n c while iterating mentioned below
for x in np.nditer(b, order = 'c'):
    print('values in x with order c are', +x)
for y in np.nditer(b, order = 'f'):
    print('values in y with order f are', +y)
#values in arrays can be modified by using op_flags parameter .. it can be set to readwrite mode or write mode
for x in np.nditer(b,op_flags=['readwrite']):
    x[...]=x*2
    print('x values r', +x)
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print(x)
#Broadcasting Iteration
#If two arrays are broadcastable, a combined nditer object is able to iterate upon them concurrently.
# Assuming that an array a has dimension 3X4, and there is another array b of dimension 1X4,
# the iterator of following type is used (array b is broadcast to size of a).
a = np.arange(0,50,5)
print(a)
a = a.reshape(2,5)
print(a)
b = np.array([1,2,3,4,5],dtype=int)
print(b)
for x,y in np.nditer([a,b]):
    print(x,y)
for x,y in np.nditer([a,b]):
    print(x*y)
