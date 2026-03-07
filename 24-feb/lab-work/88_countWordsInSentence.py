# Problem 88
# Problem Statement: Count number of words in a sentence.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

sentence = input("Enter a sentence : ")

word_count = 1
for char in sentence:
    if char == " ":
        word_count += 1

print("Sentence :", sentence)
print("Number of words :", word_count)

# output
# Enter a sentence : Python is a great language
# Sentence : Python is a great language
# Number of words : 5