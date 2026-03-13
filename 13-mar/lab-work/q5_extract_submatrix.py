# Question 5 
# Create a NumPy array of numbers from 1 to 25 and reshape it into a 5×5 matrix. 
# Extract the middle 3×3 sub-matrix. 
# Expected Output 
# [[ 7  8  9] 
# [12 13 14] 
# [17 18 19]]



import numpy as np

# Create array from 1 to 25
numbers_array = np.arange(1, 26)

# Reshape into 5x5 matrix
matrix_5x5 = numbers_array.reshape(5, 5)

# Extract middle 3x3 submatrix
middle_matrix = matrix_5x5[1:4, 1:4]

print(middle_matrix)

'''Output 
 [[ 7  8  9] 
 [12 13 14] 
 [17 18 19]]

'''