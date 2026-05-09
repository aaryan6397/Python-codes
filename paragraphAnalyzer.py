# Python program to count different types of characters

# Input paragraph from user
paragraph = input("Enter a paragraph: ")

# Initialize counters
uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

# Count characters
for ch in paragraph:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

# Store results in dictionary
result = {
    "Lowercase Letters": lowercase,
    "Uppercase Letters": uppercase,
    "Digits": digits,
    "Spaces": spaces,
    "Special Characters": special
}

# Sort in descending order of frequency
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Display results
print("\nCharacter Count (Descending Order):")
for category, count in sorted_result:
    print(category, ":", count)