# Problem 25
# Problem Statement: Find sum of even numbers up to N.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Enter the number..
num = int(input("Enter a number : "))
while num > 0:
    sum = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            sum += i
    print("Sum of even numbers up to ", num, " is : ", sum)
    break

# output
# Enter a number : 9
# Sum of even numbers up to  9  is :  20