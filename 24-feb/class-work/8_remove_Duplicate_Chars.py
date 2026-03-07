# Q8: Remove all duplicate characters from a string keeping first occurrence
# Input: "programming"
# Output: "progamin"

text = "programming"

result = ""
seen = set()

for char in text:
    if char not in seen:
        result += char
        seen.add(char)

print("Original:", text)
print("After Removing Duplicates:", result)

# Output:
# Original: programming
# After Removing Duplicates: progamin