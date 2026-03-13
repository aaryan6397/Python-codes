# Question 4 
# Create two 3×3 matrices and perform matrix multiplication. 
# Matrix A 
# [[1 2 3] 
# [4 5 6] 
# [7 8 9]] 
# Matrix B 
# [[9 8 7] 
# [6 5 4] 
# [3 2 1]] 
# Expected Output 
# [[ 30  24  18] 
# [ 84  69  54] 
# [138 114  90]]




import numpy as np

# Define Matrix A
matrix_A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Define Matrix B
matrix_B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Matrix multiplication
result_matrix = np.dot(matrix_A, matrix_B)

print(result_matrix)


'''Output 
 [[ 30  24  18] 
 [ 84  69  54] 
 [138 114  90]]
'''