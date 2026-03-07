# Problem 99
# Problem Statement: Generate all substrings of a string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

print("String :", string)
print("All substrings :")

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        print(string[i:j])

# output
# Enter a string : abc
# String : abc
# All substrings :
# a
# ab
# abc
# b
# bc
# c