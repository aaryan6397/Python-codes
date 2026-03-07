# Problem 9
# Problem Statement: Find the sum of digits of a number.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read a number from user input
number = int(input("Enter a number : "))
# initialize sum to 0
sum = 0
while number > 0:
    rem = number % 10 
    sum = sum + rem
    number = number // 10
# Print the sum of the digits
print("The sum of the digits is : ", sum)

# output
# Enter a number : 321
# The sum of the digits is :  6