import random as rd

list_of_words = ['mangos', 'bananas', 'grapes', 'oranges', 'watermelon']

random_word = rd.choice(list_of_words)
print(random_word)

def check_guess(guess):
    guess = guess.lower()
    if guess.isalpha() and len(guess) == 1:
        if guess in list(random_word):
            print(f'Good guess, {guess} is one of the letters')
        else:
            print(f"Sorry, {guess} is not in the word. Try again." )
        
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

def ask_for_input():
    while True:
        guess = input('Enter a letter: ')
        print(guess)
        check_guess(guess)

# while True:
#     ask_for_input()
        

