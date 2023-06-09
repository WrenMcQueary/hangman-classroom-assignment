"""Hangman game.  Example of a completed implementation."""


import random


#
# HELPER FUNCTIONS
#

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # file: file
    file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = file.readline()
    # word_list: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list


def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)


def is_word_guessed(secret_word, letters_guessed):
    """
    Return True if the secret word has been guessed, else false.
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    for letter in secret_word:
        if not(letter in letters_guessed):
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.  For example,
      "_ _ _ i e n i _ t _ "
    """
    # FILL IN YOUR CODE HERE...
    output_string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output_string = output_string + letter + " "
        else:
            output_string = output_string + "_ "
    return output_string


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.  For example, "bcghjkmpqstvwxyz"
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output_string = ""
    for letter in alphabet:
        if not(letter in letters_guessed):
            output_string = output_string + letter
    return output_string


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    """
    guesses_left = 8
    letters_guessed = ""
    print("Welcome to Hangman!\nI am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    while True:
        print("-------------")
        if is_word_guessed(secret_word, letters_guessed):  # If the player has won (the word has been completed):
            print("Congratulations, you won!")
            return
        elif guesses_left <= 0:     # If the player has lost:
            print("Sorry, you ran out of guesses.  The word was " + secret_word + ".")
            return
        else:   # If the game has not yet been won or lost:
            print("You have " + str(guesses_left) + " guesses left.")
            print("Available letters: " + get_available_letters(letters_guessed))
            user_guess = input("Please guess a letter: ")[0].lower()
            if user_guess in letters_guessed:   # If the user already guessed this letter before:
                print("Oops!  You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed = letters_guessed + user_guess
                if user_guess in secret_word:    # If the user guessed correctly:
                    print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                else:   # If the user guessed incorrectly:
                    guesses_left = guesses_left - 1
                    print("Oops!  That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))


WORDLIST_FILENAME = "words.txt"
wordlist = load_words()
secretWord = choose_word(wordlist).lower()
hangman(secretWord)
