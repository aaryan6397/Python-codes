# Problem 92
# Problem Statement: Find longest word in a sentence.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

sentence = input("Enter a sentence : ")

words = sentence.split(" ")

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print("Sentence :", sentence)
print("Longest word :", longest)
print("Length :", len(longest))

# output
# Enter a sentence : Python is a programming language
# Sentence : Python is a programming language
# Longest word : programming
# Length : 11