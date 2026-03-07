# Problem 45
# Problem Statement: Find sum of digits using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def sum_of_digits(num):
    total = 0
    while num > 0:
        total = total + num % 10
        num = num // 10
    return total

number = int(input("Enter a number : "))
result = sum_of_digits(number)
print("Sum of digits of", number, "is :", result)

# output
# Enter a number : 1234
# Sum of digits of 1234 is : 10