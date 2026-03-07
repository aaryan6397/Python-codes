# Problem 30
# Problem Statement: Accept numbers until 0 is entered and print sum.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

totalSum = 0
while True:
    num = int(input("Enter a number : "))
    if(num ==0):
        break
    totalSum  = totalSum + num
print("Sum of numbers is : ", totalSum)

# output
# Enter a number : 2
# Enter a number : 1
# Enter a number : 3
# Enter a number : 1
# Enter a number : 3
# Enter a number : 1
# Enter a number : 4
# Enter a number : 0
# Sum of numbers is :  15