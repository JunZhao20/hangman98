import random as rd

class Hangman:
    """
    This class is used to operate a hangman game.
    
    Attributes : 
        word_list (list) : list of words
        num_lives (int) : the number of lives the player has
        word (str) : a randomly picked word
        word_guessed (list) : a list of the letters of the word, with _ for each letter not yet guessed
        num_letters (int) : the number of unique letters that i have not been guessed yet
        list_of_guesses (list) : the list of letters have have been guessed
        
    """
    def __init__(self, word_list,num_lives=5 ):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = rd.choice(word_list)
        
        """
        Initializes word by using random module and using choice to pick one item from word_list.
        
        variable : 
            str : string of 1 random word from word_list
        """
        self.word_guessed = ['_' for i in range(len(self.word))]
        
        """
        Initializes word_guessed using list comprehension calculate the length of random word to replace with '_'
        
        variable:
            list : list of '_' wit the same number of letters in self.word
        
        """
        
        self.num_letters = len(set(self.word))
        """
        Initializes num_letters by using set() and len() to get the total unique letters within self.word
        
        variable :
            int : Number of unique letters in word
        
        """
        self.list_of_guesses = []
        

    def check_guess(self, guess):
        """
        This function is used to check the users guess to the letters in word to see if its correct or incorrect.
        
        args : 
            guess (str) : takes in guess from ask_for_input function to go through checking it with the letters in word.
        
        """
        
        guess = guess.lower()
        print(guess)
        if guess in self.word:
            print(f'Good guess, {guess} is one of the letters')
            
            index_reoccurring_letters = [index for index, value in enumerate(self.word) if value == guess]
            for index in index_reoccurring_letters:
                    self.word_guessed[index] = guess
            
            self.num_letters -= 1
            print(self.num_letters)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again." )
            print(f"You have {self.num_lives} lives left.")
        

    def ask_for_input(self):
        """
        This function is used to asks the users for a letter, it would validate the input to see if its is a alphabet and is 1 letter.
        
        """
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
                break
        
                
                
    def play_game(word_list):
        """
        This function is used to play the game.
        
        args :
            word_list (list) : takes in a guess from user to use for the random word selection.
        """
        num_lives = 5
        game = Hangman(word_list, num_lives)
        
        while True:
            
            if game.num_lives == 0:
                print('You lost!')
                break
            elif game.num_letters > 0:
                game.ask_for_input()
            else:
                print('Congratulations. You won the game!')
                break
                
        
    
    

Hangman.play_game(['mangos', 'bananas', 'grapes', 'oranges', 'watermelon'])
        




