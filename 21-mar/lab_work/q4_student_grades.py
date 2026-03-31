# Question: Student Grades System

import pandas as pd

marks = [95, 82, 67, 58, 73, 49, 88]
students = ['S1','S2','S3','S4','S5','S6','S7']

s = pd.Series(marks, index=students)

# Grade function
def grade(x):
    if x >= 90:
        return 'A'
    elif x >= 75:
        return 'B'
    elif x >= 60:
        return 'C'
    else:
        return 'D'

grades = s.apply(grade)

count = grades.value_counts()

print(grades)
print(count)

# Output:
# Grades assigned (A, B, C, D)
# Count of each grade 