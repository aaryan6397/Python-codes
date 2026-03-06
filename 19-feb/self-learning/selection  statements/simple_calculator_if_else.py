# Program: Simple calculator using selection statement

# input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# selection logic
if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    print("Result:", num1 / num2)

else:
    print("Invalid Operator")

'''output:
Enter first number: 10
Enter second number: 20
Enter operator (+, -, *, /): *
Result: 200.0
'''
    