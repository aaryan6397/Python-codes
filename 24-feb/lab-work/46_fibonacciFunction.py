# Problem 46
# Problem Statement: Generate Fibonacci series using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter the number of terms : "))
print("Fibonacci series :")
fibonacci(num)
print()

# output
# Enter the number of terms : 8
# Fibonacci series :
# 0 1 1 2 3 5 8 13