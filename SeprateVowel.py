sentence = input("Enter a sentence: ")

vowels = []
consonants = []

for ch in sentence.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels.append(ch)
        else:
            consonants.append(ch)

print("Vowels List:", vowels)
print("Consonants List:", consonants)