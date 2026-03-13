# Question 9 
# Generate a NumPy array of 10 random numbers between 0 and 1 and normalize the array between 0 
# and 1. 
# Example Output 
# Original Array: 
# [0.54 0.21 0.87 0.12 0.63 ...] 
# Normalized Array: 
# [0.56 0.12 0.95 0.00 0.67 ...]


import numpy as np

# Generate random numbers
random_array = np.random.rand(10)

# Normalize
normalized_array = (random_array - random_array.min()) / (random_array.max() - random_array.min())

print("Original Array:")
print(random_array)

print("Normalized Array:")
print(normalized_array)


'''Output 
 Original Array: 
 [0.54 0.21 0.87 0.12 0.63 ...] 
 Normalized Array: 
 [0.56 0.12 0.95 0.00 0.67 ...]'''