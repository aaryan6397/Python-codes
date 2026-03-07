# Problem 50
# Problem Statement: Calculate power using recursive function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

base = int(input("Enter base : "))
exponent = int(input("Enter exponent : "))
result = power(base, exponent)
print(base, "raised to the power", exponent, "is :", result)

# output
# Enter base : 2
# Enter exponent : 5
# 2 raised to the power 5 is : 32