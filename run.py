# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
This is Hang-Man, this game expects an input from the user and checks the array 
holding the answers to see if the user has guessed a letter in the word or not.
"""

def main_menu():
    print("Welcome to Hang-Man, the aim of the game is to guess the work before the man meets the galows! \n")
    print("Please select one of the following! \n")
    print("Start Game \n Read Instructions \n Quit Game \n")
    start_game()
    read_instructions()
    quit_game()

