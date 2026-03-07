# Q4: Count the frequency of each word in a sentence using a dictionary
# Input: "apple banana apple cherry banana apple"
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

sentence = "apple banana apple cherry banana apple"

words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Sentence:", sentence)
print("Word Frequency:", freq)

# Output:
# Sentence: apple banana apple cherry banana apple
# Word Frequency: {'apple': 3, 'banana': 2, 'cherry': 1}