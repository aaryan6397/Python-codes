# Problem 97
# Problem Statement: Count uppercase and lowercase letters.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

upper_count = 0
lower_count = 0

for char in string:
    if 'A' <= char <= 'Z':
        upper_count += 1
    elif 'a' <= char <= 'z':
        lower_count += 1

print("String :", string)
print("Uppercase letters :", upper_count)
print("Lowercase letters :", lower_count)

# output
# Enter a string : Hello World Python
# String : Hello World Python
# Uppercase letters : 3
# Lowercase letters : 13