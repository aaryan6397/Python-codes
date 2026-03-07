# unique_words.py



# Take input sentence
sentence = input("Enter a sentence: ")
# Split sentence into words and create a set of unique words
words = sentence.split()
# Create a set of unique words
unique_words = set(words)
# Print unique words and their count
print("Unique Words:", unique_words)
# Print total unique words
print("Total Unique Words:", len(unique_words))


'''output:
Enter a sentence: Hello world hello
Unique Words: {'Hello', 'hello', 'world'}
Total Unique Words: 3
'''