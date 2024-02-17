from names import names
import random
from time import sleep
from hangman_stages import stages_visual


def display_logo():
    """
    Displaying the GoT logo with a welcome message
    """
    logo = '''                                                                                                    
                    @@@@@@@@@@@@                                                                    
                 @@@@        @@@                                                                    
                @@@           @@      @         @         @@   @@@@@@@@                             
               @@@                   @@@        @@@      @@@     @@   @            @@@@             
              @@@                    @@@@       @@@     @@@@     @@        @@@@@@@ @@               
              @@@          @@@@@@   @@ @@@     @@@@@    @@@@     @@@@@@   @@ @@@ @@@@@@@            
              @@@@           @@@   @@@@@@@     @@ @@@  @@ @@@    @@   @   @@ @@@ @@@@               
               @@@@          @@@   @@   @@@    @@  @@@@@  @@@    @@        @@@@@@@ @@               
                @@@@         @@@  @@     @@@   @@   @@@   @@@    @@   @@                            
                  @@@@@     @@@@@@@@     @@@@ @@@@         @@@@ @@@@@@@                             
                     @@@@@@@@@                                                                      
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
      @     @@@                                                                              @@     
            @@@  @@@@@    @@@@@ @@@@@@@@       @@@@@@@@    @@       @@@@  @@@@@@@@   @@@@@@@@@      
            @@@    @@      @@@    @@   @@    @@@@@@@@ @@@  @@@@      @@    @@   @   @@   @@         
            @@@    @@      @@@    @@   @@@  @@@ @@@@@  @@@ @@@@@@    @@    @@       @@@             
            @@@    @@@@@@@@@@@    @@   @@   @@  @@@@@  @@@ @@  @@@   @@    @@@@@@    @@@@           
            @@@    @@      @@@    @@@@@@    @@@ @@@@@  @@@ @@   @@@@ @@    @@   @      @@@@         
            @@@    @@      @@@    @@   @@@  @@@ @@@@@  @@@ @@     @@@@@    @@           @@@         
            @@@   @@@      @@@    @@    @@@   @@@@@@@@@@   @@       @@@    @@   @@ @@   @@@         
            @@@   @@@@     @@@@ @@@@@     @@@   @@@@@     @@@@@       @   @@@@@@@   @@@@@           
           @@@@@@                                                                                   
                                                                                                    '''                                                                                                    
    print(logo)
    print("Welcome to Westeros!")
    print("\n")

def get_player_name():
    """
    Ask the user for their name input
    """
    return input("What is your name?\n")


def display_intro(name):
    """
    Display introductory message with the player's name.
    """

    print(f"You are hereby pronounced the Hero of Westeros, {name} the Great!\n")

def display_rules(name):
    """
    Rules to the game
    """
    print("You will be provided with the name of a much beloved character to guess before your tries run out\n"
         "Should you fail to guess correctly, the person will be hanged and the wrath of the Seven will rain down upon us all!\n"
         "You have 7 chances to save them! Use them visely!\n"
         "May your quest be guided by the Old Gods and the New!...\n")
    start_game(name)

def start_game(name):
    """
    Asking the user if they want to start the game
    """
    play_game = input(f"{name} the Great, are you ready to save a life today? Y/N:\n")
    if play_game == "Y":
        hangman_play()
    else:
        display_logo()

def hangman_play():
    """
    Hangman logic
    """


def main():
    display_logo()
    player_name = get_player_name()
    display_intro(player_name)
    display_rules(player_name)

if __name__ == "__main__":

    main()