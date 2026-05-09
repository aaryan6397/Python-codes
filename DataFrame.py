import numpy as np
import pandas as pd

# Generate marks array
marks = np.array([
    [85, 78, 90],
    [88, 76, 95],
    [70, 80, 85]
])

# Convert to DataFrame
df = pd.DataFrame(marks,
                  columns=["Math", "Science", "English"])

print("Student Marks DataFrame:\n")
print(df)

# Highest marks
print("\nHighest Marks:")
print(df.max())

# Average marks
print("\nAverage Marks:")
print(df.mean())

# Subject-wise statistics
print("\nSubject-wise Statistics:")
print(df.describe())