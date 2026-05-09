# Employee records
employees = [
    (101, "Amit", 50000),
    (102, "Riya", 65000),
    (103, "Karan", 45000),
    (104, "Sneha", 70000)
]

# Calculate average salary
total_salary = 0

for emp in employees:
    total_salary += emp[2]

average_salary = total_salary / len(employees)

print("Average Salary =", average_salary)

print("\nEmployees with salary above average:")

for emp in employees:
    if emp[2] > average_salary:
        print(emp)