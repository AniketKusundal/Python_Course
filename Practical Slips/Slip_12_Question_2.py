# Q.2 Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10. 


import numpy as np


matrix = np.arange(2 , 11).reshape(3 , 3)

# display the matrix

print("3 x 3 matrix with the values ranging from 2 to 10 is")
print(matrix)