# Problem 33
# Problem Statement: Print star pattern using for loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Enter the row..
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print() # New line

# Output:
# Enter number of rows: 4
# *
# **
# ***
# ****