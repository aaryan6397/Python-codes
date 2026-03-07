# Problem 76
# Problem Statement: Create student marks dictionary and find topper.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of students : "))
student_marks = {}

for i in range(n):
    name = input("Enter student name : ")
    marks = int(input("Enter marks : "))
    student_marks[name] = marks

print("Student Marks :", student_marks)

topper = ""
highest = 0
for name in student_marks:
    if student_marks[name] > highest:
        highest = student_marks[name]
        topper = name

print("Topper is :", topper, "with marks :", highest)

# output
# Enter number of students : 4
# Enter student name : Anshul
# Enter marks : 85
# Enter student name : Rahul
# Enter marks : 92
# Enter student name : Priya
# Enter marks : 78
# Enter student name : Sneha
# Enter marks : 88
# Student Marks : {'Anshul': 85, 'Rahul': 92, 'Priya': 78, 'Sneha': 88}
# Topper is : Rahul with marks : 92