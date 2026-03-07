# Problem 48
# Problem Statement: Find GCD using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
result = find_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is :", result)

# output
# Enter first number : 36
# Enter second number : 24
# GCD of 36 and 24 is : 12