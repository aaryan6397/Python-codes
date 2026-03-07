# Problem 43
# Problem Statement: Check palindrome string using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

text = input("Enter a string : ")
if is_palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")

# output
# Enter a string : madam
# madam is a Palindrome