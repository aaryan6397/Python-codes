# Question: Sales Performance Analysis

import pandas as pd

sales = [200, 450, 300, 150, 500, 700, 100]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

s = pd.Series(sales, index=days)

# Best & worst day
best = s.idxmax()
worst = s.idxmin()

# Total & average
total = s.sum()
avg = s.mean()

# Bonus 20%
bonus = s.copy()
bonus[bonus > 400] *= 1.20

# Sorted
sorted_sales = s.sort_values(ascending=False)

print("Best:", best)
print("Worst:", worst)
print("Total:", total)
print("Average:", avg)
print("With Bonus:\n", bonus)
print("Sorted:\n", sorted_sales)

# Output:
# Best day: Sat
# Worst day: Sun
# Total & average sales
# Updated bonus values
# Sorted sales