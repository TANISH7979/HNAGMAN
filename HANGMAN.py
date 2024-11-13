# Game: Hangman

import random

# List of words to guess
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = ["_"] * len(word)

# Initialize the number of lives
lives = 6

print("Welcome to Hangman!")
print("I'm thinking of a word that is", len(word), "letters long.")

while True:
    # Print the current state of the word
    print(" ".join(guessed_letters))

    # Ask the user for their guess
    guess = input("Enter a letter: ")

    # Check if the guess is in the word
    if guess in word:
        # Reveal the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
    else:
        # Decrease the number of lives
        lives -= 1
        print("Oops, that letter is not in the word. You have", lives, "lives left.")

    # Check if the user has won
    if "_" not in guessed_letters:
        print(" Congratulations! You guessed the word:", word)
        break

    # Check if the user has run out of lives
    if lives == 0:
        print("Sorry, you didn't guess the word. The word was:", word)
        break
