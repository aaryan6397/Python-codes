# Problem 89
# Problem Statement: Find frequency of each character in string.
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

print("String :", string)
print("Character frequency :")
for char in freq:
    print(char, "->", freq[char])

# output
# Enter a string : programming
# String : programming
# Character frequency :
# p -> 1
# r -> 2
# o -> 1
# g -> 2
# a -> 1
# m -> 2
# i -> 1
# n -> 1