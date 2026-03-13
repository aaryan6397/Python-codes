# Question 1 
# Create a NumPy array of numbers from 1 to 20 and reshape it into a 4×5 matrix. 
# Expected Output 
# [[ 1  2  3  4  5] 
# [ 6  7  8  9 10] 
# [11 12 13 14 15] 
# [16 17 18 19 20]]



import numpy as np

# Create array from 1 to 20
numbers_array = np.arange(1, 21)

# Reshape into 4x5 matrix
matrix_4x5 = numbers_array.reshape(4, 5)

print(matrix_4x5)


'''output:
[[1  2  3  4  5]
 [6  7  8  9  10]
 [11 12 13 14 15]
 [16 17 18 19 20]]'''


