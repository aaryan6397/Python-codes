# Question: Marks Analysis with Conditions

import pandas as pd

marks = [45, 67, 89, 34, 90, 55, 72]
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS', 'Biology', 'History']

s = pd.Series(marks, index=subjects)

# Subjects with marks > 70
above_70 = s[s > 70]

# Replace marks < 40 with "Fail"
updated = s.copy()
updated[updated < 40] = "Fail"

# Count subjects above average
avg = s.mean()
count_above_avg = (s > avg).sum()

print(above_70)
print(updated)
print(count_above_avg)

# Output:
# Chemistry    89
# CS           90
# History      72
#
# English      Fail
# (others unchanged)
#
# Count above average: 3