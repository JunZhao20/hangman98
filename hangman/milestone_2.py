import random as rd

word_list = ['mangos', 'bananas', 'grapes', 'oranges', 'watermelon']

randomWord = rd.choice(word_list)

guess = input('Enter a letter: ')

if guess.isalpha() and len(guess) == 1:
    print('Good guess')
    
else:
    print("Oops! That is not a valid input.")