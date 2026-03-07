# Problem 87
# Problem Statement: Check whether string is palindrome.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

reversed_string = ""
for i in range(len(string) - 1, -1, -1):
    reversed_string = reversed_string + string[i]

if string == reversed_string:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")

# output
# Enter a string : madam
# madam is a Palindrome