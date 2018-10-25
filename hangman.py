# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

secretWord = chooseWord(wordlist).lower()

stringAlph = "abcdefghijklmnopqrstuv"

lettersGuessed = []

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            print("_",end=" ")
        else:
            print(char,end=" ")



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    nlist = list(stringAlph)
    lst = []
    for char in nlist:
        if char not in lettersGuessed and char in nlist:
             lst.append(char)
        nrlist = ''.join(lst)
    print(nrlist)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains. 

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    gLeft = 8
    attmpts = 8
    print("The word is",len(secretWord),"characters long")
    print("You have",gLeft,"guesses left")
    
    " gLeft > 0 and "
    while gLeft > 0 or isWordGuessed(secretWord, lettersGuessed) == False or attmpts > 0:
        if gLeft > 0:
            for j in range(len(secretWord)+1):
                while isWordGuessed(secretWord, lettersGuessed) == False:
                    for i in range(attmpts):
                        r = input("Please guess a letter ")
                        if r not in lettersGuessed and r in secretWord:
                            attmpts += 1
                            print("You have",gLeft,"guesses left")
                            lettersGuessed.append(r)
                            getAvailableLetters(lettersGuessed)
                            print("Good guess: ",end=" ")
                            print(getGuessedWord(secretWord,lettersGuessed))
                            print("------------")
                            
                        elif r in lettersGuessed:
                            attmpts += 1
                            print("You have",gLeft,"guesses left")
                            print("Oops! You've already guessed that letter ",end=" ")
                            print(getGuessedWord(secretWord,lettersGuessed))
                            print("------------")
                            
                        elif r not in secretWord and r not in lettersGuessed:
                            gLeft -= 1
                            attmpts -= 1
                            lettersGuessed.append(r)
                            print("You have",gLeft,"guesses left")
                            getAvailableLetters(lettersGuessed)
                            print("Oops! That letter is not in my word ",end=" ")
                            print(getGuessedWord(secretWord,lettersGuessed))
                            print("------------")
                        if isWordGuessed(secretWord, lettersGuessed) == True:
                            break
                        if gLeft == 0:
                            break
            else:
                break
            break
        break
    print(" ")
    if gLeft <= 0:
        print("Sorry, you ran out of guesses. The word was",secretWord)
    else:
        print("Congratulations you won!!")


hangman(secretWord)
