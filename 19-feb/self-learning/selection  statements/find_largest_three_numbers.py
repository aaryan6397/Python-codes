# Program: Find the largest among three numbers
# nested if use kiya gaya hai

# input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# condition logic
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


'''output:
Enter first number: 10
Enter second number: 20 
Enter third number: 15
Largest number is: 20
'''