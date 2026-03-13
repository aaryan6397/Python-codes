# Question 10 
# Create a NumPy array of numbers from 1 to 10 and reverse the array. 
# Expected Output 
# [10 9 8 7 6 5 4 3 2 1]

import numpy as np

numbers_array = np.arange(1, 11)

reversed_array = numbers_array[::-1]

print(reversed_array)


'''Output
[10 9 8 7 6 5 4 3 2 1]'''