# Problem 93
# Problem Statement: Replace all vowels with *.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

vowels = "aeiouAEIOU"
new_string = ""

for char in string:
    if char in vowels:
        new_string = new_string + "*"
    else:
        new_string = new_string + char

print("Original string :", string)
print("Modified string :", new_string)

# output
# Enter a string : Hello World
# Original string : Hello World
# Modified string : H*ll* W*rld