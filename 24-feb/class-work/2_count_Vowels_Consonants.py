# Q2: Count the number of vowels and consonants in a string
# Input: "Hello World"
# Output: Vowels: 3, Consonants: 7


# Define the input string
text = "Hello World"
# Define vowels and initialize counts
vowels = "aeiouAEIOU"
# Initialize vowel and consonant counts
vowel_count = 0
# Initialize consonant count to 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
# Print the string, number of vowels and consonants
print("String:", text)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# Output:
# String: Hello World
# Vowels: 3
# Consonants: 7