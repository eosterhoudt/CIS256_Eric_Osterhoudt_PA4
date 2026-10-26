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


def main():
    """Start the word guessing game."""
    word = select_word()

    print("Welcome to Guess the Word!")
    print("A random word has been selected.")
    print("The word has", len(word), "letters.")


if __name__ == "__main__":
    main()
