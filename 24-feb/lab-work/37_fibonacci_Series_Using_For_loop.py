# Problem 37
# Problem Statement: Generate Fibonacci series using for loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci series:", end=" ")
for i in range(n):
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term

# Output:
# Enter number of terms: 5
# Fibonacci series: 0 1 1 2 3