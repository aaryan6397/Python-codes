# Problem 35
# Problem Statement: Count vowels in a string.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

# Enter the string ...

string = input("Enter a string : ")
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Count of vowels in the string is : ", count)

# output
# Enter a string : anshul
# Count of vowels in the string is :  2