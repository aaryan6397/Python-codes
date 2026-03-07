# Problem 90
# Problem Statement: Remove spaces from string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

new_string = ""
for char in string:
    if char != " ":
        new_string = new_string + char

print("Original string :", string)
print("String without spaces :", new_string)

# output
# Enter a string : Hello World Python
# Original string : Hello World Python
# String without spaces : HelloWorldPython