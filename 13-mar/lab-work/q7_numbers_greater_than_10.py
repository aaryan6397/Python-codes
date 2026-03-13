# Question 7 
# Create a NumPy array of numbers from 1 to 15 and find all numbers greater than 10. 
# Expected Output 
# [11 12 13 14 15]


import numpy as np

numbers_array = np.arange(1, 16)

numbers_greater_than_10 = numbers_array[numbers_array > 10]

print(numbers_greater_than_10)


'''Output 
[11 12 13 14 15]
'''


