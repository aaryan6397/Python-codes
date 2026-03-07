# Q9: Count the number of words that start with a capital letter
# Input: "India is a Great Country with Beautiful Places"
# Output: 4 (India, Great, Country, Beautiful, Places)

sentence = "India is a Great Country with Beautiful Places"

words = sentence.split()
count = 0
capital_words = []

for word in words:
    if word[0].isupper():
        count += 1
        capital_words.append(word)

print("Sentence:", sentence)
print("Words starting with Capital:", capital_words)
print("Count:", count)

# Output:
# Sentence: India is a Great Country with Beautiful Places
# Words starting with Capital: ['India', 'Great', 'Country', 'Beautiful', 'Places']
# Count: 5