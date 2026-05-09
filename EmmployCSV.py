import pandas as pd

# Read CSV file
df = pd.read_csv("employees.csv")

# Department-wise average salary
print("Department-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())

# Highest salary employee
highest = df.loc[df["Salary"].idxmax()]

print("\nHighest Salary Employee:")
print(highest)