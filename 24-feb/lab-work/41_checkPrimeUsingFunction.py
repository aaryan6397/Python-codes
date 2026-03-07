# Problem 41
# Problem Statement: Check prime number using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number : "))
if is_prime(number):
    print(number, "is a Prime number")
else:
    print(number, "is not a Prime number")

# output
# Enter a number : 7
# 7 is a Prime number