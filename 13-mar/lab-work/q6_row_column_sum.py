
# Question 6 
# Create a 4×4 matrix and calculate: 
# • Row-wise sum 
# • Column-wise sum 
# Example Matrix 
# [[1 2 3 4] 
# [5 6 7 8]
# [9 10 11 12] 
# [13 14 15 16]] 
# Expected Output 
# Row Sum: 
# [10 26 42 58] 
# Column Sum: 
# [28 32 36 40]

import numpy as np

matrix_4x4 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

# Row-wise sum
row_sum = np.sum(matrix_4x4, axis=1)

# Column-wise sum
column_sum = np.sum(matrix_4x4, axis=0)

print("Row Sum:")
print(row_sum)

print("Column Sum:")
print(column_sum)


'''Output 
 Row Sum: 
 [10 26 42 58] 
 Column Sum: 
 [28 32 36 40]
'''