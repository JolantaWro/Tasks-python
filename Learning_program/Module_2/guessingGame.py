#!/usr/bin/env python3
import random

# Initialize variables
wrongGuesses = 7
guessed = False
correctLetters = []
wrongLetters = []

with open('wordlist.txt', 'r') as words:
    tempList = words.readlines()

words = []
for word in tempList:
    words.append(word.rstrip('\n'))

indexNumber = random.randint(0, (len(words)-1))

def processGuess(turn, guess, wrongGuesses):
    blanks = ''
    validLetter = False

    if guess in word:
            validLetter = True

    if validLetter == True:
        if turn != 1:
            correctLetters.append(guess)
            print('Correct!', 'The letter', guess, 'is in the word.')
    else:
        if turn != 1:
            wrongLetters.append(guess)
            wrongGuesses = wrongGuesses - 1
            print("I'm sorry,", guess, "is not in the word.")
        print('You have', wrongGuesses, 'wrong guesses left.')

    lettersGuessedCorrect = 0
    for letter in word:
        letterInWord = False
        if letter in correctLetters:
            letterInWord = True
            lettersGuessedCorrect = lettersGuessedCorrect + 1
        
        if letterInWord is True:
            blanks = blanks + letter + ' '
        else:
            blanks = blanks + '_ '

    print(blanks)
    return lettersGuessedCorrect, wrongGuesses

word = words[indexNumber]

processGuess(1, '', wrongGuesses)
turn = 2

while guessed is False and wrongGuesses > 0:

    print('Correct Letters Guessed: ', correctLetters)
    print('Wrong Letters Guessed: ', wrongLetters)

    guess = input('What letter would you like to guess?').lower()

    newLetter = True
    if guess in wrongLetters:
            newLetter = False
    if guess in correctLetters:
            newLetter = False

    if newLetter is False:
        print("I'm sorry, you already guessed that letter.")
        continue
    elif guess.isdigit() is True:
        print("I'm sorry, you can only guess letters.")
        continue

    lettersGuessedCorrect, wrongGuesses = processGuess(turn, guess, wrongGuesses)    

    if len(word) == lettersGuessedCorrect:
        print('You have guessed the word! You had', wrongGuesses, 'wrong guesses left.')
        guessed = True
if wrongGuesses == 0:
    print('Too bad! the word was:', word)
    print("I'm sorry, you lose.")
else:
    print('Congratulations! You win!')

print('Please play again!')