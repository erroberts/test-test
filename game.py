import random

WORD = ('dinosaur')
word = (WORD)
correct = word
clue = word[0] + word[(len(word)-1):(len(word))]
letter_guess = ''
word_guess = ''
store_letter = ''
count = 0
limit = 10

print('Welcome to "Night Schools Guess Word Game!"')
print('You have 10 attempts at guessing LETTERS in the secret word')
print('Let\'s begin!')
print('\n')

while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('Right on the money!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('Sorry that is incorrect')
        count += 1

    if count == 2:
        print('\n')
        clue_request = input('Would you like a clue?')
        if clue_request == 'y':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        if clue_request == 'n':
            print('Wow, you must be brave')

print('\n')
print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
print('These letters are: ', store_letter)
final = input('final guess time. Guess the Word: ')
if final != WORD:
        print(word)
if final == WORD:
    print('You are correct! You must of googled it!')

    
    
