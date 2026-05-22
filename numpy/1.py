import numpy as np
print(np.__version__)


#CREATING ARRAYS FROM LISTS
arr_1d = np.array([1,2,3,4,5])
print("1-D array is \n",arr_1d)
arr_2d = np.array([[1,2,3],[4,5,6]])
print("2-D array is \n",arr_2d)

#list vs numpy arrays
my_list = [1,2,3,4]
my_list *= 2
print("List multiplication result \n",my_list)

arr = np.array([1,2,3])
arr *= 2
print("array multiplication result \n " , arr)

# time of operation 
import time
start = time.time()
py_list = [i*2 for i in range(1000000)]
print("List operation time is \n", time.time() - start)

start = time.time()
num1 = np.arange(1000000)*2
print("Numpy operation time is \n", time.time() - start)


