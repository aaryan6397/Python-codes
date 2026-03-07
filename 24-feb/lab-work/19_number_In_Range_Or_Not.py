# Problem 19
# Problem Statement: Check whether a number lies within a given range.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read a number and the range from user input
num = float(input("Enter a number : "))
lower_bound = float(input("Enter the lower bound of the range : "))
upper_bound = float(input("Enter the upper bound of the range : ")) 
if(lower_bound <= num <= upper_bound):
    print("The number lies within the range.")
else: 
    print("The number does not lie within the range.")

# output
# Enter a number : 21
# Enter the lower bound of the range : 0
# Enter the upper bound of the range : 12
# The number does not lie within the range.