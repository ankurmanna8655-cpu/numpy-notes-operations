#array slicing

import numpy as np

arr = np.array([1,2,3,4,5])
print("Basic Slicing \n", arr[2:5])
print("Step slicing \n",arr[0:5:2])
print("Negative slicing \n",arr[-3])

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [6,7,8]])
print("specific element in a matrix(row) \n", arr_2d[1,2])

print("Entire row \n", arr_2d[1])

print("Entire column \n", arr_2d[:,1])

unsorted = np.array([3,6,1,5,8,3,5,9])
print("Sorted array is \n", np.sort(unsorted))

arr_2d_unsorted = np.array([[1,2],[5,6],[9,10]])
print("Sorted 2D array by column \n", np.sort(arr_2d_unsorted , axis=0))

arr_2d_unsorted1 = np.array([[2,1],[5,4],[11,5]])
print("Sorted 2D array by row \n", np.sort(arr_2d_unsorted1 , axis=1))

#filter
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
filter_num = numbers[numbers % 2 == 0]
print("Even numbers from array are \n",filter_num)

#filter with mask
mask = numbers > 5
print("Mask numbers from array are(Numbers greater than 5) \n", numbers[mask])

#fancy indexing vs np.where
indices = [0 ,2, 4]
print("Fancy indexing numbers \n", numbers[indices])

where = np.where(numbers > 5, numbers * 5 , numbers)
where1 = np.where(numbers > 5 , True , False)

print("First where clause \n", where)
print("Second where clause \n", where1)

#Adding and removing data
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
add = arr1 + arr2
print("Added result \n", add)

combined = np.concatenate((arr1,arr2))
print("Combined array \n",combined)

original_array = np.array([[1,2],[3,4]])
new_row = np.array([5,6])
with_new_row = np.vstack((original_array,new_row))
print("Added new row \n",with_new_row)

new_column = np.array([[7],[8]])
with_new_column = np.hstack((original_array,new_column))
print("Added new column \n",with_new_column)

#array compatability
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
print("comapatability shapes ", a.shape == b.shape)

my_arr = np.array([1,2,3,4,5,6])
nt = np.delete(my_arr,2)
print("Array after deletion ", nt)


