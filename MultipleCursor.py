# Tuples containing student names and courses
course1 = ("Amit", "Riya", "Karan", "Sneha")
course2 = ("Riya", "Aman", "Karan", "Pooja")

# Convert tuples to sets
set1 = set(course1)
set2 = set(course2)

# Students enrolled in multiple courses
common_students = set1.intersection(set2)

print("Students enrolled in multiple courses:")
print(common_students)