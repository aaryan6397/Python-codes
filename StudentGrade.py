import pandas as pd

# Create DataFrame
data = {
    "Name": ["Amit", "Riya", "Karan"],
    "Math": [85, 90, 70],
    "Science": [80, 95, 75],
    "English": [78, 88, 72]
}

df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Calculate percentage
df["Percentage"] = df["Total"] / 3

# Grade function
def grade(p):

    if p >= 90:
        return "A+"

    elif p >= 75:
        return "A"

    elif p >= 60:
        return "B"

    else:
        return "C"

# Assign grades
df["Grade"] = df["Percentage"].apply(grade)

print(df)