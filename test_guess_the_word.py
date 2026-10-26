# Eric Osterhoudt
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import WORDS, select_word, display_word


# Test that the randomly selected word comes from the word list
def test_select_word():
    word = select_word()
    assert word in WORDS


# Test that a correct guess reveals the correct letter
def test_correct_guess():
    word = "python"
    guessed_letters = ["p"]

    result = display_word(word, guessed_letters)

    assert result == "p _ _ _ _ _"


# Test that an incorrect guess does not reveal any letters
def test_incorrect_guess():
    word = "python"
    guessed_letters = ["z"]

    result = display_word(word, guessed_letters)

    assert result == "_ _ _ _ _ _"


# Test that letters can be guessed in any order
def test_multiple_guesses():
    word = "python"
    guessed_letters = ["o", "p", "t"]

    result = display_word(word, guessed_letters)

    assert result == "p _ t _ o _"


# Test that all instances of a repeated letter are revealed
def test_repeated_letters():
    word = "letter"
    guessed_letters = ["t"]

    result = display_word(word, guessed_letters)

    assert result == "_ _ t t _ _"
