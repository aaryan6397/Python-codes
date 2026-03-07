# Problem 42
# Problem Statement: Find factorial using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

number = int(input("Enter a number : "))
result = factorial(number)
print("Factorial of", number, "is :", result)

# output
# Enter a number : 5
# Factorial of 5 is : 120