"""Hangman game.  Complete the functions marked "TODO".
"""


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
    pass    # TODO: Implement


def is_word_guessed(secret_word, letters_guessed):
    """
    Return True if the secret word has been guessed, else false.
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    pass    # TODO


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.  For example,
      "_ _ _ i e n i _ t _ "
    """
    pass    # TODO


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.  For example, "bcghjkmpqstvwxyz"
    """
    pass    # TODO


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
        # TODO: Check if the player has won (the word has been completed).  If so, congratulate the player for winning and end the game
        # TODO: Check if the player has lost (is out of guesses).  If so, tell the player they've lost, tell them what the secret word was, and end the game.
        # TODO: Tell the player how many guesses are left, and which letters they haven't chosen yet.  Then have them guess a new letter.  Reject repeat letters but don't dock them a guess.  Then show them the portion of the word they've guessed so far.


WORDLIST_FILENAME = "words.txt"
wordlist = load_words()
secretWord = choose_word(wordlist).lower()
hangman(secretWord)
