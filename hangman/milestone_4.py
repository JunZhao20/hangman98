import random as rd

class Hangman:
    
    def __init__(self, word_list,num_lives=5 ):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = rd.choice(word_list)
        self.word_guessed = ['_' for i in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        

    def check_guess(self, guess):
        guess = guess.lower()
        print(guess)
        if guess in self.word:
            print(f'Good guess, {guess} is one of the letters')
            for letter in self.word:
                if guess == letter:
                    self.word_guessed[self.word.index(letter)] = guess
            self.num_letters -= 1
            print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again." )
            print(f"You have {self.num_lives} lives left.")
        

    def ask_for_input(self):
        while True:
            print(self.word)
            print(self.word_guessed)
            guess = input('Enter a letter: ')
            if guess.isalpha() is not True and len(guess) != 1:
                print('Invalid letter')
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

player1 = Hangman(['mangos', 'bananas', 'grapes', 'oranges', 'watermelon'])

player1.ask_for_input()