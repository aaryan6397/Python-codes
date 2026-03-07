# Problem 22
# Problem Statement: Find factorial using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Enter the numbers ..
num = int(input("Enter a number : "))
fact = 1
i=1
while num >=i:
    fact = fact * i
    i = i + 1

print("Fcatorial of", num, "is", fact)

# output
# Enter a number : 5
# Fcatorial of 5 is 120