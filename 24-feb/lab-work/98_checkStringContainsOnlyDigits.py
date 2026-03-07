# Problem 98
# Problem Statement: Check whether string contains only digits.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

only_digits = True
for char in string:
    if char < '0' or char > '9':
        only_digits = False
        break

print("String :", string)
if only_digits:
    print("String contains only digits")
else:
    print("String does not contain only digits")

# output
# Enter a string : 12345
# String : 12345
# String contains only digits