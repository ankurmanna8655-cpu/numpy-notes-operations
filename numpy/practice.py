# 1.Statistical Functions

# Find:

# mean
# median
# standard deviation
# maximum
# minimum
#arr = np.array([2,4,6,8,10])

import numpy as np

arr = np.array([2,4,6,8,10])
print("mean of the result is \n",np.mean(arr))

print("median of result is \n",np.median(arr))

print("standard deviation of the result \n",np.std(arr))

print("maximum element from array \n", np.max(arr))

print("minimum from the array is \n", np.min(arr))

# 2. Random Arrays

# Create:

# random integers between 1–100
# a 5×5 random float matrix
# set a random seed
arr3 = np.random.seed(42)

arr1 = np.random.randint(1,101,size=10)
print("integer random \n",arr1)

arr2 = np.random.random((5,5))
print("float random \n",arr2)

#3. From:

# arr = np.array([12,5,8,130,44])

# Get:

# elements greater than 10
# even numbers only

arr4 = np.array([12,5,8,130,44])
n = arr4 > 5 
print("elements greater than 5 are \n",arr4[n])

even_num = arr4[arr4 % 2 == 0]
print("even numbers are \n",even_num)

# 4. Unique Elements

# Find:

# unique elements
# count of each unique element

arr5 = np.array([1,2,2,3,3,3,4])
unique_elements,count = np.unique(arr5, return_counts=True)
print("Unique elemnts \n",unique_elements)
print("Count of elements \n",count)

for elements,counts in zip(unique_elements,count):
    print(f"{elements} occurs {counts} times")

