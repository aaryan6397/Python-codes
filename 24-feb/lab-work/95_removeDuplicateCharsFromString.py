# Problem 95
# Problem Statement: Remove duplicate characters from string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

new_string = ""
for char in string:
    if char not in new_string:
        new_string = new_string + char

print("Original string :", string)
print("String after removing duplicates :", new_string)

# output
# Enter a string : programming
# Original string : programming
# String after removing duplicates : progamin