# Program: Count digits in a number
# Loop type: while loop

# input
num = int(input("Enter a number: "))

count = 0

# loop jab tak number 0 nahi hota
while num != 0:
    num //= 10   # last digit remove
    count += 1

print("Total digits =", count)


'''output:
Enter a number: 12345
Total digits = 5
'''