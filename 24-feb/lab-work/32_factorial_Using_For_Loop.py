# Problem 32
# Problem Statement: Find factorial using for loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Enter the number..
num = int(input("Enter aa number : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("factorial of ", num, "is : ", fact)

# output
# Enter aa number : 5
# factorial of  5 is :  120