# Problem 85
# Problem Statement: Find sum of all dictionary values.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of items : "))
my_dict = {}
for i in range(n):
    key = input("Enter key : ")
    value = int(input("Enter value : "))
    my_dict[key] = value

print("Dictionary :", my_dict)

total = 0
for key in my_dict:
    total = total + my_dict[key]

print("Sum of all dictionary values is :", total)

# output
# Enter number of items : 4
# Enter key : a
# Enter value : 10
# Enter key : b
# Enter value : 20
# Enter key : c
# Enter value : 30
# Enter key : d
# Enter value : 40
# Dictionary : {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# Sum of all dictionary values is : 100