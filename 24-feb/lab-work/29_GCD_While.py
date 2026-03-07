# Problem 29
# Problem Statement: Find GCD using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


num1 = int(input("Enter a first number :"))
num2 = int(input("Enter a second number :"))
while num1 != num2:
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1
print("GCD is : ", num1)

# output
# Enter a first number :15   
# Enter a second number :25
# GCD is :  5