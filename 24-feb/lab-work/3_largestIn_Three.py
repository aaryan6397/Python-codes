# Problem 3
# Problem Statement: Find the largest of three numbers.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read three numbers from user input
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if(num1 >= num2 and num1 >= num3):
    print("The largest number is : ", num1)
elif(num2 >= num1 and num2 >= num3):
    print("The largest number is : ", num2)
else:
    print("The largest number is : ", num3)

# Enter first number: 10
# Enter second number: 25
# Enter third number: 15
# The largest number is: 25