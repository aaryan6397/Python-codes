import numpy as np

# Create 5x5 matrix with random integers
matrix = np.random.randint(1, 100, (5, 5))

print("Matrix:\n", matrix)

# Row-wise sum
print("\nRow-wise Sum:")
print(matrix.sum(axis=1))

# Column-wise sum
print("\nColumn-wise Sum:")
print(matrix.sum(axis=0))

# Transpose
print("\nTranspose of Matrix:")
print(matrix.T)

# Determinant
print("\nDeterminant:")
print(np.linalg.det(matrix))