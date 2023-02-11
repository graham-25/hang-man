# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
This is Hang-Man, this game expects an input from the user and checks the array 
holding the answers to see if the user has guessed a letter in the word or not.
"""
import random

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
    This function starts the game, its going to randomly select a word from the array.    
    """
    lst = []
    word_list = ["octipuss", "banana", "frog"]
    word = random.choice(word_list)
    print(word)
    len_word = len(word)
    print("The length of the word is ", len_word)
    find_word = " - " * len_word
    print(find_word)
    x = input("Please select a letter or a guess word! \n")
    
    for letter in x:
        lst.append(letter)
 
    print(lst)

    #for i in range(choice.index(choice[-1]) +1):
    #print(choice[i])
    #txt = choice.index(word)
    #print(txt)
    #find_letter = choice.index(word, 0)
    #print(find_letter)
    #guess = choice.isalpha()
    #print(guess)
    #result = word.index(str(choice))
    #print(result)

def check_answer():
    """
    This function checks the user answer to see if their guess is in the chosen letter. 
    """

def read_instructions():
    """
    This function tells the user how to play the game,
    """


def quit_game():
    """
    This function quits the game.
    """

main_menu()