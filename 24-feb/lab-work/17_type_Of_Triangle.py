# Problem 17
# Problem Statement: Determine the type of triangle.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read the lengths of the sides of the triangle from user input
s1 = float(input("Enter the length of side 1: "))
s2 = float(input("Enter the length of side 2: "))
s3 = float(input("Enter the length of side 3: "))

if s1 == s2 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Output:
# Enter the length of side 1: 5
# Enter the length of side 2: 5
# Enter the length of side 3: 8
# Isosceles Triangle