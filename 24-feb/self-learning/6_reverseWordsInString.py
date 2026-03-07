# Q6: Reverse the order of words in a string
# Input: "Hello World Python"
# Output: "Python World Hello"

sentence = "Hello World Python"

words = sentence.split()
words.reverse()
reversed_sentence = " ".join(words)

print("Original:", sentence)
print("Reversed Words:", reversed_sentence)

# Output:
# Original: Hello World Python
# Reversed Words: Python World Hello