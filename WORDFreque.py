# Read text file
file = open("sample.txt", "r")

text = file.read().lower()
file.close()

# Remove punctuation
for ch in ",.!?;:":
    text = text.replace(ch, "")

words = text.split()

frequency = {}

# Count word frequencies
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Sort dictionary by frequency
sorted_words = sorted(frequency.items(),
                      key=lambda x: x[1],
                      reverse=True)

print("Top 5 Most Frequently Used Words:\n")

for word, count in sorted_words[:5]:
    print(word, ":", count)