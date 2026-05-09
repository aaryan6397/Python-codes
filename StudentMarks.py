# Create and read student marks file

students = {
    "Amit": 85,
    "Riya": 92,
    "Karan": 70,
    "Sneha": 60
}

# Write data to file
file = open("marks.txt", "w")

for name, marks in students.items():
    file.write(name + " " + str(marks) + "\n")

file.close()

# Read file
file = open("marks.txt", "r")

data = {}
total = 0

for line in file:
    name, marks = line.split()
    marks = int(marks)
    data[name] = marks
    total += marks

file.close()

# Average
average = total / len(data)

# Topper
topper = max(data, key=data.get)

print("Topper:", topper, "-", data[topper])

print("Average Marks:", average)

print("\nStudents scoring below average:")

for name, marks in data.items():
    if marks < average:
        print(name, "-", marks)