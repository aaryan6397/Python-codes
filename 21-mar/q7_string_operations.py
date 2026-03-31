# Question: String Operations in Series

import pandas as pd

names = ['anuj', 'rahul', 'sneha', 'kiran', 'amit']
s = pd.Series(names)

# Uppercase
upper = s.str.upper()

# Names containing 'a'
contains_a = s[s.str.contains('a')]

# Replace name
replaced = s.replace('anuj', 'Anuj Kumar')

print(upper)
print(contains_a)
print(replaced)

# Output:
# All uppercase names
# Names containing 'a'
# Updated names