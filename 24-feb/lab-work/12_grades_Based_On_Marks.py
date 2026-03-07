# Problem 12
# Problem Statement: Assign grades based on marks.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


marks = float(input("Enter marks: "))

if(marks < 0 or marks > 100):
    print("Invalid marks. Please enter a value between 0 and 100.")
else:
    
    if marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print("Grade:", grade)

# Output:
# Enter marks: 85
# Grade: B