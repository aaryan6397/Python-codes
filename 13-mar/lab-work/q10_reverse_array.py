# Question 10 
# Create a NumPy array of numbers from 1 to 10 and reverse the array. 
# Expected Output 
# [10 9 8 7 6 5 4 3 2 1]

import numpy as np

numbers_array = np.arange(1, 11)
print("Befor reversing array : ")
print(numbers_array)

reversed_array = numbers_array[::-1]
print("After the reversing array : ")

print(reversed_array)


'''Output
Befor reversing array : 
[ 1  2  3  4  5  6  7  8  9 10]
After the reversing array :
[10  9  8  7  6  5  4  3  2  1]'''