#array syntax
import numpy as np
a = np.array([1,2,3,4])
print(a)
#two dimensions (result shows with two square brackets)
b = np.array([[1,2,3],[4,5,6]])
print(b)
#ndmin specifies the minimum dimensions of resultant array
c = np.array([1,2,3,4], ndmin=2) #If I give ndmin = 3(3 dimensions)here it gives result with 3 square brackets
print(c)
#dtype is a desired datatype of an array
a = np.array([1,2,3,4], dtype=complex)
print(a)
a = np.array([1,2,3,4], dtype=str)
print(a)
#Data Type Objects (dtype)
d = np.dtype(np.float)
print(d)
##int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.
dt = np.dtype('i8')
print(dt)
# using endian notation
dt = np.dtype('>i4')
print(dt)
dt = np.dtype([('age',np.int8)])
print(dt)
## first create structured data type
#In case of structured type, the names of fields,
# data type of each field and part of the memory block taken by each field.
dto = np.dtype([('name','S5')])
ax = np.array([('Siri'),('purni')],dtype=dto)
print(ax)
print(ax['name'])
#The following examples define a structured data type called student with a string field 'name',
# an integer field 'age' and a float field 'marks'
dt = np.dtype([('name','S10'),('age','i8'),('marks','f8')])
a = np.array([('siri',20,30),('purni',10,50)], dtype=dt)
print(a)
#---------------------------------------------
#array attributes
a = np.array([[1,2,3,4],[3,4,5,6]])
print(a.shape)
#array can be reshaped using a.shape function
a.shape = (4,2)
print(a)
#NumPy also provides a reshape function to resize an array.
b = a.reshape(4,2)
print(b)
#ndarray.ndim
#This array attribute returns the number of array dimensions.
a = np.arange(24)
print(a)
print(a.ndim)
b = a.reshape(4,2,3)
print(b)
b = a.reshape(2,4,3)
print(b)
print(b.ndim)
#numpy.itemsize This array attribute returns the length of each element of array in bytes.
c = np.array([1,2,3,4,5],dtype=np.int8)
print(c.itemsize)
#numpy.flags
#The ndarray object has the following attributes. Its current values are returned by this function.
print(c.flags)
#numpy.empty
#The following code shows an example of an empty array
x = np.empty([3,2],dtype=np.int8)
print(x)
#np.zeros
x = np.zeros((5,),dtype=np.int)
print(x)
#convert a list to ndarray(n dimentional array) using asarray function
x = [1,2,3,4]
a = np.asarray(x,dtype=int)
print(a)
#convert a tuple
x = (1,2,3,4)
a = np.asarray(x,dtype=float)
print(a)
#list of typles
x = [(1,2,3,4),(4,5,6,8)]
a = np.asarray(x,dtype=int)
print(a)
#numpy.frombuffer
#This function interprets a buffer as one-dimensional array.
"""
s = 'Hello World'
a = np.frombuffer(s,dtype=int)
print(a)
"""
a = np.arange(20)
print(a[1:20:2])
print(a[1:])
print(a[:5:2])
a = np.array([[1,2,3,4],[12,8,9,20],[34,56,78,90]])
print(a[1:])
print(a[:1])
print(a[1,3])
print(a)
#Advanced slicing of arrays
#column1
print(a[...,1] )
#column3
print(a[...,3])
#row1
print(a[1,...])
#from column 1
print(a[...,1:])
print(a)
b = a[[0,1,2],[0,1,0]] #it takes as 0,0 and 1,1 and 2,0
print(b)
#----------
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)
#-----------
#advanced indexing for column
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print('after slicing array becomes')
print(x[1:4])
print(x[1:3])
print(x[1:2,1:3])
print(x[1:4,1:3])
print(x[1,2])
print(x[1:4,[1,2]])
#boolean
print('greater than 5 are ', +x[x>5])
#remove NaN numbers(Not a Number) using ~ (complement operator)
y = np.array([np.nan,1,2,np.nan,4,5])
print('elements in y are', +y)
print(y[~np.isnan(y)])
#to filterout non complex elements
z = np.array([1, 2+6j, 5, 6+7j])
print(z[np.iscomplex(z)])
#self-exercise of indexing and advanced indexing
n = np.array([[5,4,10,15,6],[20,25,16,18,21],[23,32,42,45,46],[48,50,55,60,62]])
print(n)
print(n[0,2])
print(n[0:2])
print(n[2:3])
print(n[1,4])
print(n[2,1])
print(n[3,2])
print(n[3,4])
print(n[1:])
print(n[:1])
print(n[1,])
print(n[...,1])
print(n[...,2])
print(n[...,3])
print(n[...,1:3])
print(n[[1,1,1],[0,1,2]],n[[2,2,2],[0,2,2]])
a = np.array([[1,1,1],[2,2,2]])
b = np.array([[0,1,2],[0,2,2]])
c = n[a,b]
print(c)