# Program: Swap two numbers without third variable

# input             
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# swapping logic
a = a + b
b = a - b
a = a - b

# output
print("After swapping")
print("a =", a)
print("b =", b)


'''output:
Enter first number: 10
Enter second number: 20

After swapping
a = 20
b = 10
'''