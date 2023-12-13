import random as rd

list_of_words = ['mangos', 'bananas', 'grapes', 'oranges', 'watermelon']

randomWord = rd.choice(list_of_words)

guess_letter = input('Enter a letter: ')


def guess_input_validation(guess_letter):
    if guess_letter.isalpha() and len(guess_letter) == 1:
        print('Good guess')
        
    else:
        print("Oops! That is not a valid input.")