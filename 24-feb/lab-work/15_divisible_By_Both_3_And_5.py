# Problem 15
# Problem Statement: Check whether a number is divisible by both 3 and 5.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read a number from user input..
num = int(input("Enter a number : "))
if(num % 3 == 0 and num % 5 == 0):
    print("Divisible by both 3 and 5")
else:
    print("Not Divisible by both 3 and 5")

# # output
# Enter a number : 15
# Divisible by both 3 and 5