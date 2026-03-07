# Problem 44
# Problem Statement: Find maximum of three numbers using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
result = maximum_of_three(num1, num2, num3)
print("Maximum of three numbers is :", result)

# output
# Enter first number : 10
# Enter second number : 25
# Enter third number : 15
# Maximum of three numbers is : 25