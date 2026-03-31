# Question: Chained Operations

import pandas as pd

data = [5, None, 15, 25, None, 35, 45]
s = pd.Series(data)

result = (
    s.fillna(s.median())
     .loc[lambda x: x > 20]
     .sort_values(ascending=False)
     .reset_index(drop=True)
)

print(result)

# Output:
# Values > 20 sorted descending with reset index