# Q11: Compress a string by counting consecutive repeated characters
# Input: "aaabbcdddde"
# Output: "a3b2c1d4e1"

text = "aaabbcdddde"

compressed = ""
i = 0

while i < len(text):
    count = 1
    while i + count < len(text) and text[i] == text[i + count]:
        count += 1
    compressed += text[i] + str(count)
    i += count

print("Original:", text)
print("Compressed:", compressed)

# Output:
# Original: aaabbcdddde
# Compressed: a3b2c1d4e1