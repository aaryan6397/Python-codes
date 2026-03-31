# Question: Series Alignment

import pandas as pd

s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([5, 15, 25], index=['B', 'C', 'D'])

# Addition
result = s1 + s2

# Replace NaN with 0
result_filled = result.fillna(0)

print(result)
print(result_filled)

# Output:
# A   NaN
# B   25
# C   45
# D   NaN
#
# After fill:
# A   0
# B   25
# C   45
# D   0