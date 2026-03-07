# Problem 94
# Problem Statement: Check whether two strings are anagrams.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

sorted_str1 = sorted(str1.lower())
sorted_str2 = sorted(str2.lower())

if sorted_str1 == sorted_str2:
    print(str1, "and", str2, "are Anagrams")
else:
    print(str1, "and", str2, "are not Anagrams")

# output
# Enter first string : listen
# Enter second string : silent
# listen and silent are Anagrams