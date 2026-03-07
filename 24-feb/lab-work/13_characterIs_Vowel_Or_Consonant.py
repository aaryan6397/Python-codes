
# Program to check if a character is a vowel or consonant
# Problem Statement: Check whether a character is a vowel or consonant.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Read a character from user input
char = input("Enter a character: ")

# Convert to lower case for easy comparison
char = char.lower() 
if(char.isalpha()):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input. Please enter a single alphabetic character.")



# Output:
# Enter a character: E
# Vowel