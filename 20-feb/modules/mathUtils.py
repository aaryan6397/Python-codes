

# This module contains basic mathematical operations such as addition, subtraction, multiplication, and division.

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"
    


# there are two ways to use these functions, either by passing arguments directly or by taking user input and then passing those inputs to the functions.




# direct arguments


'''a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))

# using functions....

sum_result = add_numbers(a, b)
diff_result = subtract_numbers(a, b)
product_result = multiply_numbers(a, b)
division_result = divide_numbers(a, b)

# printing results.....

print("Sum: ",sum_result)
print("Difference: ",diff_result)
print("Product: ",product_result)
print("Division: ",division_result)'''


# taking user input inside the functions and then calling those functions to perform operations.


'''def add_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 + num2

def subtract_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 - num2

def multiply_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1 * num2

def divide_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"
 
        
# calling functions to perform operations....

sum_result = add_numbers()
diff_result = subtract_numbers()
product_result = multiply_numbers()
division_result = divide_numbers()

# printing results.....

print("Sum: ",sum_result)
print("Difference: ",diff_result)
print("Product: ",product_result)
print("Division: ",division_result)
'''
