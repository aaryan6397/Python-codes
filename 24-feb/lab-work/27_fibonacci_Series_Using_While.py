# Problem 27
# Problem Statement: Generate Fibonacci series using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Enter the numbers..
num = int(input("Enter a number : "))
a = 0
b=1
i=1
while i <= num:
    print(a, end=" ")
    c = a + b 
    a = b
    b = c
    i = i + 1

# output
# Enter a number : 8
# 0 1 1 2 3 5 8 13 