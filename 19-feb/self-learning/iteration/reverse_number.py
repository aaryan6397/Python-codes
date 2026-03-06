# Program: Reverse a number

# input
num = int(input("Enter a number: "))

reverse = 0

# loop
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number =", reverse)




'''output:
Enter a number: 12345
Reversed number = 54321
'''
