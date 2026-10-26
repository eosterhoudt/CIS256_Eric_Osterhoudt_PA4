# Eric Osterhoudt
# CIS256 Fall 2026
# Programming Assignment 4

import random


# List of possible words for the game
WORDS = [
    "python",
    "computer",
    "program",
    "keyboard",
    "software",
    "internet",
    "database",
    "variable"
]


def select_word():
    """Select and return a random word from the word list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Display guessed letters and hide letters not guessed yet."""
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.strip()


def main():
    """Run the word guessing game."""
    word = select_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Guess the Word!")
    print("Guess the word one letter at a time.")
    print("You have", attempts, "incorrect attempts.")

    # Continue playing until the word is guessed or attempts reach zero
    while attempts > 0:
        print()
        print("Word:", display_word(word, guessed_letters))
        print("Attempts remaining:", attempts)

        guess = input("Enter a letter: ").lower()

        # Make sure the user enters one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        # Prevent the same letter from being guessed more than once
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check whether the guessed letter is in the word
        if guess in word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess.")

        # Check whether every letter in the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print()
            print("Congratulations! You guessed the word:", word)
            return

    print()
    print("You ran out of attempts.")
    print("The word was:", word)


if __name__ == "__main__":
    main()
