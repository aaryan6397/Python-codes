# Problem 96
# Problem Statement: Find first non-repeating character in string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

freq = {}
for char in string:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

result = ""
for char in string:
    if freq[char] == 1:
        result = char
        break

print("String :", string)
if result != "":
    print("First non-repeating character is :", result)
else:
    print("No non-repeating character found")

# output
# Enter a string : aabbcdd
# String : aabbcdd
# First non-repeating character is : c