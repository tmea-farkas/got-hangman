from words import words
import random, os
from hangman_stages import stages_visual
from colorama import init, Fore
init(autoreset= True)


class C: # adapted from code aquired from Matt Bodden
    '''
    C class contains the terminal color shortcuts
    for use when printing things to the terminal
    '''
    RED = '\33[91m'
    GREEN = '\33[32m'

def display_logo():
    """
    Displaying the logo with a welcome message
    """
    logo = '''                                       
        ┌──────────────────────────────────────────────────────────────┐
        │  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████    █████▒      │
        │ ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██   ▒       │
        │▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒▒████ ░       │
        │░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░░▓█▒  ░       │
        │░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░░▒█░          │
        │ ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░  ▒ ░          │
        │      ░       ░  ░       ░      ░  ░       ░ ░                │
        │                                                              │
        │▄▄▄█████▓ ██░ ██  ██▀███   ▒█████   ███▄    █ ▓█████   ██████ │
        │▓  ██▒ ▓▒▓██░ ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ │
        │▒ ▓██░ ▒░▒██▀▀██░▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒███   ░ ▓██▄   │
        │░ ▓██▓ ░ ░▓█ ░██ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒│
        │  ▒██▒ ░ ░▓█▒░██▓░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░░▒████▒▒██████▒▒│
        │  ▒ ░░    ▒ ░░▒░▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░│
        │  ░       ░  ░░ ░  ░░   ░ ░ ░ ░ ▒     ░   ░ ░    ░   ░  ░  ░  │
        └──────────────────────────────────────────────────────────────┘
                                                        '''
    print(Fore.LIGHTRED_EX + logo)
    print("Welcome to Westeros! The Game of Thrones inspired Hangman Game \n")

def clear_window():
    """
    Clear display window for better user experience
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_player_name():
    """
    Ask the user for their name input, validating it to contain only letters
    """
    while True:
        name = input("What is your name?\n").capitalize()
        if name.isalpha() and len(name) <= 10:
            return name
        else:
            print("If we sought an epic tale, we'd employ dragons for missives, not mere crows.")


def display_intro(name):
    """
    Display introductory message with the player's name.
    """
    clear_window()
    print("\n")
    print(f"By the decree of the Seven Kingdoms, let it be known that {name} the Fearless, is henceforth proclaimed as the Hero of Westeros! \n")

def display_rules(name):
    """
    Rules to the game
    """
    print("Prepare yourself, for you are tasked with the sacred duty of guessing the name of a beloved character before your attempts expire.\n")
    print("Fail, and the dire consequences shall befall them, with the wrath of the Seven descending upon us all!\n")
    print("You are granted but 7 chances to rescue them from the abyss. Choose wisely, for the fate of Westeros hangs in the balance!\n")
    print("\n")
    print("May your quest be guided by the Old Gods and the New!...\n")
    print("\n")
    start_game(name)

def start_game(name):
    """
    Asking the user if they want to start the game
    """
    while True:
        play_game = input(f"{name} the Fearless, are you ready to save a life today? Y/N:\n").upper()
        print("\n")
        if play_game == "Y":
            word = get_name()
            hangman_play(word)
            break
        elif play_game == "N":
            display_logo()
            name = get_player_name()  # Prompt the user for their name again
        else:
            print("Choose now to venture forth by entering 'Y', or delay your journey by selecting 'N' if you're not yet prepared to face the challenges ahead.")
            print("\n")
        clear_window()
def get_name():
    """
    Getting a random word from the words list
    """
    word = random.choice(words)
    return word



def hangman_play(word): # code adapted from Youtube tutorial
    """
    Hangman logic
    """
    clear_window() #keep
    word_completion = "".join(["_" if char != " " else " " for char in word])
    guessed = False
    guessed_letters = []
    guessed_words = []
    guesses = 7
    print("Let us begin!")
    print(stages_visual(guesses))
    print(word_completion)
    print("\n")
    while not guessed and guesses > 0:
        print(f"You have {guesses} guesses left")
        print("Letters guessed so far: ", ",".join(guessed_letters))
        print("\n")
        guess = input("Please guess a letter: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Fore.LIGHTRED_EX + "You already guessed the letter", guess)
            elif guess not in word:
                print(guess, Fore.LIGHTRED_EX + " is not in the word.")
                guesses -= 1
                guessed_letters.append(guess)
            else:
                print("\n")
                print(Fore.GREEN + "Great! You're one step closer to being a True Hero!")
                guessed_letters.append(guess)
                word_to_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_to_list[index] = guess
                word_completion = "".join(word_to_list)
                if word_completion == word:
                    guessed = True
        else:
            print(Fore.RED + "Not a valid guess")
        print(stages_visual(guesses))
        print(word_completion)
        print("\n")
    if guessed:
        print("What do we say to the God of Death?...")
        print("\n")
        print(word + " is alive for another day because of you!")
        play_again()
    else:
        print(f"The victim was {word}, and is now dead!")
        print("Looks like the Gods are not in your favour today! Better luck next time, ey!")
        play_again()

def play_again():
    while input("What about another round?(Y/N) \n").upper() == "Y":
        print("\n")
        word = get_name()
        hangman_play(word)
    else:
        print("See you next time!")
        print("\n")
        clear_window()
        display_logo()

def main():
    display_logo()
    player_name = get_player_name()
    display_intro(player_name)
    display_rules(player_name)
    start_game(player_name)
    word = get_name()
    hangman_play(word)
    play_again()

if __name__ == "__main__":

    main()