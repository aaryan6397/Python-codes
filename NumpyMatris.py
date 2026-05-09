import numpy as np

# Create matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Addition
print("Addition:\n", A + B)

# Subtraction
print("\nSubtraction:\n", A - B)

# Multiplication
print("\nMultiplication:\n", np.dot(A, B))

# Inverse
print("\nInverse of Matrix A:\n", np.linalg.inv(A))

print("\nInverse of Matrix B:\n", np.linalg.inv(B))