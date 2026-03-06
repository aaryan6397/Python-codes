

# This module demonstrates how to import and use functions from another module (mathUtils) to perform basic mathematical operations.
#whole module import karne ke liye import mathUtils as  shortname in module for example "cal" ka use kar sakte hain, jahan cal ek alias hai jo mathUtils module ko refer karta hai.



# first step is to create a module named mathUtils.py and define functions for addition, subtraction, multiplication, and division in that module. Then we can import those functions in this file and use them to perform operations on user input numbers.


''' import mathUtils as cal

num1 = int(input("Enter first number: "))
 
num2 = int(input("Enter second number: "))

sum_res = cal.add_numbers(num1,num2)
sub_res = cal.subtract_numbers(num1,num2)
print("Sum:",sum_res)
print("Difference:",sub_res)

'''

# importing functions from mathUtils module and then using those functions to perform operations.
# from mathUtils import add_numbers, subtract_numbers
# whole module import karne ke liye * ka use kar sakte hain.


#second way is to import specific functions from the mathUtils module and then use those functions directly without the need for a module alias.

from mathUtils import *

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_res = add_numbers(num1,num2)
sub_res = subtract_numbers(num1,num2)
print("Sum:",sum_res)
print("Difference:",sub_res)

# output
# Enter first number: 10
# Enter second number: 5
# Sum: 15
# Difference: 5