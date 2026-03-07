# Problem 79
# Problem Statement: Sort dictionary by keys.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n = int(input("Enter number of items : "))
my_dict = {}
for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    my_dict[key] = value

print("Original dictionary :", my_dict)

sorted_keys = sorted(my_dict)
sorted_dict = {}
for key in sorted_keys:
    sorted_dict[key] = my_dict[key]

print("Dictionary sorted by keys :", sorted_dict)

# output
# Enter number of items : 4
# Enter key : d
# Enter value : 4
# Enter key : b
# Enter value : 2
# Enter key : a
# Enter value : 1
# Enter key : c
# Enter value : 3
# Original dictionary : {'d': '4', 'b': '2', 'a': '1', 'c': '3'}
# Dictionary sorted by keys : {'a': '1', 'b': '2', 'c': '3', 'd': '4'}