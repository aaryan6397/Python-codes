# Problem 39
# Problem Statement: Calculate power without using exponent operator.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for i in range(exp):
    result = result * base
print("Result:", result)

# Output:
# Enter base: 2
# Enter exponent: 3
# Result: 8