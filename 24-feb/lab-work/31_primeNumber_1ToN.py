# Problem 31
# Problem Statement: Print all prime numbers between 1 and N.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

num = int(input("Enter a number : "))
print("Prime numbers between 1 and ", num, " are : ")
for i in range(2, num + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i, end=" ")



# output
# Enter a number : 90
# Prime numbers between 1 and  90  are : 
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 % 