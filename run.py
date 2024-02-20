from words import words
import random
from time import sleep
from hangman_stages import stages_visual


def display_logo():
    """
    Displaying the GoT logo with a welcome message
    """
    logo = '''                                                                                                    
        ┌──────────────────────────────────────────────────────────────┐
        │  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████    █████▒      │
        │ ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██   ▒       │
        │▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒▒████ ░       │
        │░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░░▓█▒  ░       │
        │░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░░▒█░          │
        │ ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░  ▒ ░          │
        │  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░  ░            │
        │░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒   ░ ░          │
        │      ░       ░  ░       ░      ░  ░       ░ ░                │
        │                                                              │
        │▄▄▄█████▓ ██░ ██  ██▀███   ▒█████   ███▄    █ ▓█████   ██████ │
        │▓  ██▒ ▓▒▓██░ ██▒▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▒██    ▒ │
        │▒ ▓██░ ▒░▒██▀▀██░▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒███   ░ ▓██▄   │
        │░ ▓██▓ ░ ░▓█ ░██ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒│
        │  ▒██▒ ░ ░▓█▒░██▓░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░░▒████▒▒██████▒▒│
        │  ▒ ░░    ▒ ░░▒░▒░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░│
        │    ░     ▒ ░▒░ ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░│
        │  ░       ░  ░░ ░  ░░   ░ ░ ░ ░ ▒     ░   ░ ░    ░   ░  ░  ░  │
        │          ░  ░  ░   ░         ░ ░           ░    ░  ░      ░  │
        └──────────────────────────────────────────────────────────────┘
                                                        '''
    print(logo)
    print("Welcome to Westeros!")
    print("\n")

def get_player_name():
    """
    Ask the user for their name input, validating it to contain only letters
    """
    while True:
        name = input("What is your name?\n")
        if name.isalpha() and len(name) <= 10:
            return name
        else:
            print("If we sought an epic tale, we'd employ dragons for missives, not mere crows.")


def display_intro(name):
    """
    Display introductory message with the player's name.
    """

    print(f"By the decree of the Seven Kingdoms, let it be known that {name}, the Fearless, is henceforth proclaimed as the Hero of Westeros! \n")

def display_rules(name):
    """
    Rules to the game
    """
    print("Prepare yourself, for you are tasked with the sacred duty of guessing the name of a beloved character before your attempts expire\n"
         "Fail, and the dire consequences shall befall them, with the wrath of the Seven Kingdoms descending upon us all!\n"
         "You are granted but 7 chances to rescue them from the abyss. Choose wisely, for the fate of Westeros hangs in the balance!\n"
         "May your quest be guided by the Old Gods and the New!...\n")
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
            print("Please enter 'Y' to start the game, or 'N' if you're not ready to")
            print("\n")

def get_name():
    """
    Getting a random word from the words list
    """
    word = random.choice(words)
    return word



def hangman_play(word):
    """
    Hangman logic
    """
    word_completion = "".join(["_" if char != " " else " " for char in word])
    guessed = False
    guessed_letters = []
    guessed_words = []
    guesses = 7
    print("Let's begin!")
    print(stages_visual(guesses))
    print(word_completion)
    print("\n")
    while not guessed and guesses > 0:
        print(f"You have {guesses} guesses left")
        guess = input("Please guess a letter or the name: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                guesses -= 1
                guessed_letters.append(guess)
            else:
                print("Great! You're one step closer to being a True Hero")
                guessed_letters.append(guess)
                word_to_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_to_list[index] = guess
                word_completion = "".join(word_to_list)
                if word_completion == word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
                guesses -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
        print(stages_visual(guesses))
        print(word_completion)
        print("\n")
    if guessed:
        print("What do we say to the God of Death?...")
        print("\n")
        print(word + " is alive for another day because of you!")
        play_again()
    else:
        print(f"The victim was {word}, and is now dead")
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