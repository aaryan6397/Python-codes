# Problem 47
# Problem Statement: Count vowels using function.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string : ")
result = count_vowels(text)
print("Count of vowels in the string is :", result)

# output
# Enter a string : anshul
# Count of vowels in the string is : 2