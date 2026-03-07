# Problem 91
# Problem Statement: Convert string to title case manually.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

title_string = ""
capitalize_next = True

for char in string:
    if char == " ":
        title_string = title_string + char
        capitalize_next = True
    else:
        if capitalize_next and 'a' <= char <= 'z':
            title_string = title_string + chr(ord(char) - 32)
            capitalize_next = False
        else:
            title_string = title_string + char
            capitalize_next = False

print("Original string :", string)
print("Title case string :", title_string)

# output
# Enter a string : hello world python
# Original string : hello world python
# Title case string : Hello World Python