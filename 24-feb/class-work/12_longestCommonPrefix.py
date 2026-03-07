# Q12: Find the longest common prefix among a list of strings
# Input: ["flower", "flow", "flight"]
# Output: "fl"

words = ["flower", "flow", "flight"]

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            break

print("Words:", words)
print("Longest Common Prefix:", prefix)

# Output:
# Words: ['flower', 'flow', 'flight']
# Longest Common Prefix: fl