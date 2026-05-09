try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result =", num1 + num2)

    elif op == "-":
        print("Result =", num1 - num2)

    elif op == "*":
        print("Result =", num1 * num2)

    elif op == "/":
        print("Result =", num1 / num2)

    else:
        print("Invalid Operation!")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input entered.")

except Exception as e:
    print("Unexpected Error:", e)