# Q3: Create a dictionary from a string to store character frequency
# Input: "programming"
# Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}


# Define the input string
word = "programming"

# Create an empty dictionary to store character frequency
char_freq = {}
for char in word:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
# Print the string and the character frequency dictionary
print("String:", word)
print("Character Frequency:", char_freq)



# Output:
# String: programming
# Character Frequency: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}