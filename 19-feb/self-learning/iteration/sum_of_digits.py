# Program: Find sum of digits of a number

# input
num = int(input("Enter a number: "))

total = 0

# loop
while num != 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits =", total)

'''output:
Enter a number: 12345
Sum of digits = 15


Explanation:
The program calculates the sum of digits of a given number using a while loop. It extracts each
digit by taking the modulus of 10, adds it to the total, and then removes the last digit by performing integer division by 10. Finally, it prints the result.
'''