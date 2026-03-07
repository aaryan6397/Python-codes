# Q9: Check if a string is a pangram (contains every letter of the alphabet)
# Input: "The quick brown fox jumps over the lazy dog"
# Output: True (it is a pangram)

sentence = "The quick brown fox jumps over the lazy dog"

alphabet = set("abcdefghijklmnopqrstuvwxyz")
sentence_letters = set(sentence.lower())

is_pangram = alphabet.issubset(sentence_letters)

print("Sentence:", sentence)
print("Is Pangram:", is_pangram)

# Checking with a non-pangram
sentence2 = "Hello World"
is_pangram2 = alphabet.issubset(set(sentence2.lower()))
print("\nSentence:", sentence2)
print("Is Pangram:", is_pangram2)

# Output:
# Sentence: The quick brown fox jumps over the lazy dog
# Is Pangram: True
#
# Sentence: Hello World
# Is Pangram: False