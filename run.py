from names import names
import random
from logo import got_logo
from hangman_stages import stages_visual


def display_logo():
    """
    Displaying the welcome message and ascii logo imported from logo.py
    """
    print("Welcome to Westeros \n")
    print(got_logo)


def get_player_name():
    """
    Ask the user for their name input
    """
    return input("What is your name?\n")


def display_intro(name):
    """
    Display rules as introductory message with the player's name.
    """

    print(f"You are hereby pronounced the Hero of Westeros, {name} the Great!\n"
         "You will be provided with the name of a much beloved character to guess before your tries run out\n"
         "Should you fail to guess correctly, the person will be hanged and the wrath of the Seven will rain down upon us all!\n"
         "You have 7 chances to save them! Use them visely!\n"
         "May your quest be guided by the Old Gods and the New!...\n")

def main():
    display_logo()
    player_name = get_player_name()
    display_intro(player_name)

if __name__ == "__main__":

    main()