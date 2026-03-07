# Problem 23
# Problem Statement: Reverse a number using while loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# enter the number ...
number = int(input("Enter a number : "))
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print("Reverse of the number is : ", reverse)

# output
# Enter a number : 221
# Reverse of the number is :  122