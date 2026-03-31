# Question: Handling Missing Data

import pandas as pd

data = [10, None, 30, None, 50, 60, None]
s = pd.Series(data)

# Count before
before = s.isnull().sum()

# Fill with mean
s_filled = s.fillna(s.mean())

# Count after
after = s_filled.isnull().sum()

# Drop remaining nulls
s_clean = s_filled.dropna()

print("Before:", before)
print("After:", after)
print(s_clean)

# Output:
# Before: 3
# After: 0
# Series with no null values