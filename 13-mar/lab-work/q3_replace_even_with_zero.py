# Question 3 
# Create a NumPy array of numbers from 1 to 10 and replace all even numbers with 0. 
# Expected Output 
# [1 0 3 0 5 0 7 0 9 0]

import numpy as np

# Create array from 1 to 10
numbers_array = np.arange(1, 11)

# Replace even numbers with 0
numbers_array[numbers_array % 2 == 0] = 0

print(numbers_array)



'''output :
 [1 0 3 0 5 0 7 0 9 0]'''