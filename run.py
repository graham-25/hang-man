# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
This is Hang-Man, this game expects an input from the user and checks the array 
holding the answers to see if the user has guessed a letter in the word or not.
"""

def main_menu():
    """
    
    """
    print("Welcome to Hang-Man, the aim of the game is to guess the work before the man meets the galows! \n")
    print("Please select one of the following! \n")
    print("\n Start Game: 1\n Read Instructions: 2\n Quit Game: 3\n")
    option = int(input("Please select a game option! \n"))
    if option == 1:
        start_game()
    elif option == 2:
        read_instructions()
    elif option == 3:
        quit_game()

def start_game():
    """
    This function starts the game,     
    """
    choice_words = ['octipuss', 'banana', 'frog']
def option():
    """
    This function tells the user how to play the game,
    """
def quit_game():
    """
    This function quits the game.
    """