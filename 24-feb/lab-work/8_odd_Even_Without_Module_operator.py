# Problem 8
# Problem Statement: Check whether a number is even or odd without modulus operator.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Read a number from user input
number = int(input("Enter a number : "))
# To check if the number is even or odd without using modulus operator, we can use integer division and multiplication.
num = (number // 2) * 2

if(num == number):
    print("Number is Even")
else :
    print("Number is Odd")

# output
# Enter a number : 213
# Number is Odd