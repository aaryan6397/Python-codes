# Problem 78
# Problem Statement: Merge two dictionaries manually.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

n1 = int(input("Enter number of items in dictionary 1 : "))
dict1 = {}
for i in range(n1):
    key = input("Enter key : ")
    value = input("Enter value : ")
    dict1[key] = value

n2 = int(input("Enter number of items in dictionary 2 : "))
dict2 = {}
for i in range(n2):
    key = input("Enter key : ")
    value = input("Enter value : ")
    dict2[key] = value

merged = {}
for key in dict1:
    merged[key] = dict1[key]
for key in dict2:
    merged[key] = dict2[key]

print("Dictionary 1 :", dict1)
print("Dictionary 2 :", dict2)
print("Merged dictionary :", merged)

# output
# Enter number of items in dictionary 1 : 2
# Enter key : a
# Enter value : 1
# Enter key : b
# Enter value : 2
# Enter number of items in dictionary 2 : 2
# Enter key : c
# Enter value : 3
# Enter key : d
# Enter value : 4
# Dictionary 1 : {'a': '1', 'b': '2'}
# Dictionary 2 : {'c': '3', 'd': '4'}
# Merged dictionary : {'a': '1', 'b': '2', 'c': '3', 'd': '4'}