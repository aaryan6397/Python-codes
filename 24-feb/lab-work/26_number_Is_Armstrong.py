# Problem 26
# Problem Statement: Check whether a number is Armstrong.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Enter the number...
num = int(input("Enter a number: "))
n = num
power = len(str(num))

total = 0

while n > 0:
    digit = n % 10
    total += digit ** power
    n //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# output
# Enter a number: 153
# Armstrong Number