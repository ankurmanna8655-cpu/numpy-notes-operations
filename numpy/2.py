#Creating arrays from scratch
import numpy as np
zeros = np.zeros((2,3))
print("zeroes arrays \n", zeros)

ones = np.ones((2,3))
print("ones arrays \n", ones)

full = np.full((2,3),5)
print("full arrays \n", full)

random = np.random.random((2,3))
print("random array \n",random)

sequence = np.arange(0 , 11 , 2)
print("sequence array \n",sequence)

# vector , matrix and tenser

vector = np.array([1,2,3,4])
print("Vector is\n", vector)

matrix = np.array([[1,2,3],[3,4,5]])
print("Matrix is\n", matrix)

tensor = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Tensor is\n", tensor)

#Array properties

array_1 = np.array([[1,2,3],
                        [4,5,6]])
print("array shape \n",array_1.shape)
print("array dimension \n",array_1.ndim)
print("array size \n",array_1.size)
print("array dtype \n",array_1.dtype)

# Array reshaping

arr = np.arange(12)
print("original array \n",arr)

reshaped = arr.reshape((3,4))
print("reshaped array \n", reshaped)

flattened = reshaped.flatten()
print("flattened array \n", flattened)

#raveled (returns view instead of copy)
raveled = reshaped.ravel()
print("raveled array \n", raveled)

#transpose
transpose = reshaped.T
print("Transposed array \n",transpose)