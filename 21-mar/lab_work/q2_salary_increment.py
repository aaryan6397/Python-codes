# Question: Salary Increment Logic

import pandas as pd

salary = [25000, 32000, 28000, 40000, 50000]
emp = ['A', 'B', 'C', 'D', 'E']

s = pd.Series(salary, index=emp)

# Increase 10% if < 30000
s[s < 30000] *= 1.10

# Decrease 5% if > 45000
s[s > 45000] *= 0.95

total = s.sum()

print(s)
print("Total Salary:", total)

# Output:
# Updated salaries after increment/decrement
# Total Salary: (calculated value)