# Problem 36
# Problem Statement: Print all divisors of a number.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


num = int(input("Enter a number : "))
print("Divisors of ", num, "are : ")
for i in range(1, num+1):
    if num % i == 0:
        print(i)  
# output
# Enter a number : 12
# Divisors of  12 are : 
# 1
# 2
# 3 
# 4
# 6
# 12