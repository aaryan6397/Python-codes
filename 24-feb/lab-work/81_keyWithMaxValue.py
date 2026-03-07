# Problem 81
# Problem Statement: Find key with maximum value.
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

max_key = ""
max_value = 0
first = True
for key in my_dict:
    if first or my_dict[key] > max_value:
        max_value = my_dict[key]
        max_key = key
        first = False

print("Key with maximum value is :", max_key, "with value :", max_value)

# output
# Enter number of items : 4
# Enter key : a
# Enter value : 10
# Enter key : b
# Enter value : 45
# Enter key : c
# Enter value : 30
# Enter key : d
# Enter value : 20
# Dictionary : {'a': 10, 'b': 45, 'c': 30, 'd': 20}
# Key with maximum value is : b with value : 45