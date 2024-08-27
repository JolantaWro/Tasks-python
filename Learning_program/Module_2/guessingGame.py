#!/usr/bin/env python3

word = input('Please enter a word for your opponent: ')

# Initialize variables
wrongGuesses = 7
guessed = False
correctLetters = ''
wrongLetters = ''
blanks = ''

for letter in word:
    blanks = blanks+'_ '

print(blanks)