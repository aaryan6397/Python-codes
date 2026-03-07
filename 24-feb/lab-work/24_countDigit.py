# Problem 24
# Problem Statement: Count digits in a number.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Enter the numbers...
number = int(input("Enter a number : "))
count = 0
while number > 0:
    number = number // 10
    count +=1
print("Count of digits in the number is : ", count)

# output
# Enter a number : 12456
# Count of digits in the number is :  5