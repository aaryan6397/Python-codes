# Problem 4
# Problem Statement: Calculate simple interest.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Read principal, rate of interest, and time from user input
p = float(input("Enter Principal: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (years): "))

simple_interest = (p * r * t) / 100

print("Simple Interest is:", simple_interest)

# Output:
# Enter Principal: 1000
# Enter Rate of interest: 5
# Enter Time (years): 2
# Simple Interest is: 100.0