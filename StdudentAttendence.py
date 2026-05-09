import pandas as pd

# Read CSV file
df = pd.read_csv("attendance.csv")

# Display students with attendance below 75%
low_attendance = df[df["Attendance"] < 75]

print("Students with Attendance below 75%:\n")

print(low_attendance)