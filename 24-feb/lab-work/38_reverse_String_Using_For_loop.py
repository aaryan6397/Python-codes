# Problem 38
# Problem Statement: Reverse a string using for loop.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed string:", reversed_text)

# Output:
# Enter a string: python
# Reversed string: nohtyp