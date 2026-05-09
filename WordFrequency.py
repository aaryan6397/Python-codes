paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequencies:")
print(frequency)

# Most repeated word
most_repeated = max(frequency, key=frequency.get)

print("\nMost Repeated Word:", most_repeated)
print("Count:", frequency[most_repeated])