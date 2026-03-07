# Problem 77
# Problem Statement: Count character frequency using dictionary.
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

print("Character frequency :")
for key in freq:
    print(key, "->", freq[key])

# output
# Enter a string : hello
# Character frequency :
# h -> 1
# e -> 1
# l -> 2
# o -> 1