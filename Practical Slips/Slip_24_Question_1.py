# Q.1 Write a NumPy program to get the unique elements of an array.


import numpy as np

arr = np.array([1, 2, 3, 4, 2, 99 , 70 , 80])

unique_elements = np.unique(arr)

print("Orignal Array" , arr)
print("Unique Elements in Numpy Array" , unique_elements)