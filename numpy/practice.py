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

# 5. Mini Marks Analysis

# Create marks of 5 students in 3 subjects using NumPy.

# Find:

# average marks per student
# topper
# subject-wise highest marks

marks = np.array([
    [85, 90, 78],
    [88, 76, 92],
    [90, 91, 89],
    [70, 65, 80],
    [95, 88, 84]
])

#1.
print("Average marks per student is :",np.mean(marks,axis =1))

#2.
topper_marks = np.sum(marks,axis =1)
print("Total Marks of each student is :",topper_marks)

topper_index = np.argmax(topper_marks)
print(f"Topper is student {topper_index+1} ")

#3.
print("Subjectwise highest marks is :",np.max(marks,axis=0))

#6. Create a border of 1s around a matrix of 0s.

# Example:

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1

new_matrix = np.ones((4,5))

new_matrix[1:-1,1:-1] = 0      
#  arr[1:-1, 1:-1] ows from index 1 to second-last columns from index 1 to second-last
print(new_matrix)

# 7. Given daily temperatures:

# temps = np.array([30,32,31,29,35,36,34])

# Find:

# hottest day
# coldest day
# days above average

temps = np.array([30,32,31,29,35,36,34])
hottest_temp = np.max(temps)
hottest_day = np.argmax(temps)
print(f"Hottest is DAY: {hottest_day+1} and hottest temp is {hottest_temp}")

coldest_temp = np.min(temps)
coldest_day = np.argmin(temps)
print(f"Coldest is DAY: {coldest_day+1} and coldest temp is {coldest_temp}")

avg_temp = np.mean(temps)
above_avg = temps > avg_temp
above_avg_index = np.argmax(temps)
print(f"Temperatures above averages are :{temps[above_avg]} ")