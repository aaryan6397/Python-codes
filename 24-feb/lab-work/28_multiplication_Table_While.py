# Problem 28
# Problem Statement: Print multiplication table using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply


# Enter the number ...
num = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(num, "X", i, "=", num * i)
    i = i + 1

# output
# Enter a number : 4
# 4 X 1 = 4
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36
# 4 X 10 = 40