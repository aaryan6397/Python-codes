# Q10: Extract all digits from a string and find their sum
# Input: "hello123world45python6"
# Output: Digits: [1, 2, 3, 4, 5, 6], Sum: 21

text = "hello123world45python6"

digits = []
for char in text:
    if char.isdigit():
        digits.append(int(char))

total = sum(digits)

print("String:", text)
print("Digits Found:", digits)
print("Sum of Digits:", total)

# Output:
# String: hello123world45python6
# Digits Found: [1, 2, 3, 4, 5, 6]
# Sum of Digits: 21