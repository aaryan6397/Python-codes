# Problem 100
# Problem Statement: Compress a string using character counts.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

string = input("Enter a string : ")

compressed = ""
i = 0

while i < len(string):
    count = 1
    while i + count < len(string) and string[i] == string[i + count]:
        count += 1
    compressed = compressed + string[i] + str(count)
    i = i + count

print("Original string :", string)
print("Compressed string :", compressed)

# output
# Enter a string : aaabbbccdd
# Original string : aaabbbccdd
# Compressed string : a3b3c2d2