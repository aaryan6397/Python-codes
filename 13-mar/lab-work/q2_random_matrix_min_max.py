# Question 2 
# Create a 5×5 matrix with random integers between 1 and 100 and find: 
# • Minimum value 
# • Maximum value 
# Example Output 
# Matrix: 
# [[23 45 12 89 34] 
# [67 11 90 54 32] 
# [76 28 19 47 65] 
# [14 73 52 39 81] 
# [60 21 48 70 16]] 
# Min = 11 
# Max = 90 
# (Values may vary because of random numbers.)



import numpy as np

# Generate 5x5 random matrix
random_matrix = np.random.randint(1, 101, (5, 5))

# Find min and max values
minimum_value = np.min(random_matrix)
maximum_value = np.max(random_matrix)

print("Matrix:")
print(random_matrix)

print("Min =", minimum_value)
print("Max =", maximum_value)


'''output:
Matrix: 
[[23 45 12 89 34] 
[67 11 90 54 32] 
[76 28 19 47 65] 
[14 73 52 39 81] 
[60 21 48 70 16]] 
Min = 11 
Max = 90 
'''