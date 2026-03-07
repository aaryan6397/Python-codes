# Problem 1
# Problem Statement: Swap two numbers without using a third variable.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read two numbers from user input
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number :"))

# Print the numbers before swapping
print("Before swaping num1 : ", num1)
print("Before swaping num2 : ", num2)

# swaping logic

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Print the numbers after swapping
print("after swaping num1 : ", num1)
print("after swaping num2 : ", num2)
