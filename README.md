Welcome to the Game of Thrones Hangman!

![Game window]()
[Game of Thrones Hangman](https://got-hangman-46eee30c0ce3.herokuapp.com/)

# The project
This project is a classic Hangman game with a theme applied from the popular TV Show Game of Thrones. This is represented by not only the logo, but the guessable character names and wording of the game creating the illusion of a quest for the player, essentially involving them in the story.

# The Scope
The scope of the project was to create a game that is easily navigated, engaging and can be played multiple times even by a returning user.
## UX
## As a user
- First-time user
- Returning user
## As the developer
# Design
From a design perspective I aimed to stay within the theme of Game of Thrones. As well as wording, colours and theme.
# Features
1. The background
I chose to put a background image to further improve user experience
![background image]()
2. Logo
Logo was created by ASCIIART.eu from an image of the Game of Thrones logo
![GoT Logo]()
3. Favicon
The favicon was added to further elevate user satisfaction
![GoT Favicon]()
4. Colour coordinated messages
    - Green colour for positive reinforcement
![Green message]()
    - Red for failed input
![Red message]()
5. Y/N choice questions
For easy navigation Yes or No questions were implemented where appropriate to ensure the user of a good flow of navigation through the game
![Y/N questions]()
6. Input validation
Input validation has been implemented wherever user input was requested to avoid undesired input being accepted therefore damaging user experience.
![Input validation]()

## Features left to implement
At a future stage, I am planning to implement a score keeping system by using an API to keep a list of the top 10 players and give the user feedback if they are on the list once they have finished playing.

# Technologies

- Python language to develop the project
- VSCode as the project IDE
- Colorama to add colours to print messages
- Vecteezy to get SVG background image
- ASCIIART.eu to create ascii art of Game of Thrones logo
- Favicon.io to generate favicon

# Deployment

# Testing
The project has gone through continuous testing during development using print messages at every stage. Has been tested by several users.
It has also been tested by pep8 standards which provided no issues with the code.
# Bugs
- cearing the window at the wrong line
    - moved the clear_window() function call to the relevant places
- indentation issue with print statements
    - fixed by adjusting the indentation
- not taking the user back to the top at the end of the game
    - called the relevant function at the end

# Credits

Code written by me with the help of:

- Matthew Bodden - my mentor
- Slack colleagues
- Youtube tutorials - ex.: https://www.youtube.com/watch?v=m4nEnsavl6w&t=173s

Thank you!

