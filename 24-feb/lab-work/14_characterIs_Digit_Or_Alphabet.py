# Problem 14
# Problem Statement: Check whether a character is digit or alphabet.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


# Read a character from user input
ch = input("Enter something: ")
# To check whether the character is a digit or an alphabet, we can use the built-in string methods isalpha() and isdigit().
if(ch.isalpha()):
    print("Alphabet")
elif(ch.isdigit()):
    print("Digit")
elif(ch.isalnum()):
    print("character is alphanumeric")
else:
    print("Special Character")

# Output:
# Enter something: 5
# Digit