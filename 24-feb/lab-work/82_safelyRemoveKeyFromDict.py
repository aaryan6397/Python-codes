# Problem 82
# Problem Statement: Safely remove a key from dictionary.
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

remove_key = input("Enter key to remove : ")

if remove_key in my_dict:
    del my_dict[remove_key]
    print("Key", remove_key, "removed successfully")
else:
    print("Key", remove_key, "not found in dictionary")

print("Updated dictionary :", my_dict)

# output
# Enter number of items : 3
# Enter key : a
# Enter value : 1
# Enter key : b
# Enter value : 2
# Enter key : c
# Enter value : 3
# Original dictionary : {'a': '1', 'b': '2', 'c': '3'}
# Enter key to remove : b
# Key b removed successfully
# Updated dictionary : {'a': '1', 'c': '3'}