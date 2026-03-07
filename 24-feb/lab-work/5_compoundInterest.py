# Problem 5
# Problem Statement: Calculate compound interest.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

# 2. Calculate the total amount
# We use ** for "to the power of"
amount = p * (1 + r / 100)**t

ci = amount - p

print("Compound Interest is:", ci)

# output
# Enter Principal: 1000
# Enter Rate: 10
# Enter Time: 2
# Compound Interest is: 210.00