# Program: Simple number guessing game
# Loop continues until correct number guessed

secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again.")


'''output:
Guess the number: 5
Wrong guess. Try again.
Guess the number: 7
Correct! You guessed the number.
'''