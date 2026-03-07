# Problem 10
# Problem Statement: Reverse a given number.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Read a number from user input
number = int(input("Enter a number : "))
# Store the original number for later use
orgNum = number
# Initialize the variable to store the reversed number
rev = 0
while number > 0:
    rem = number % 10 
    rev = rev * 10 + rem
    number = number // 10
# Print the original number and the reversed number
print("Original Number is : ", orgNum)
print("Reverse of the Number is : ", rev)

# output
# Enter a number : 311
# Original Number is :  311
# Reverse of the Number is :  113