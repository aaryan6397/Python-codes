# Problem 86
# Problem Statement: Reverse a string without slicing.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

reversed_string = ""
for i in range(len(string) - 1, -1, -1):
    reversed_string = reversed_string + string[i]

print("Original string :", string)
print("Reversed string :", reversed_string)

# output
# Enter a string : hello
# Original string : hello
# Reversed string : olleh