Welcome to the Game of Thrones Hangman!

![Game window](https://github.com/tmea-farkas/got-hangman/blob/main/images/hangman.png)
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
![background image](https://github.com/tmea-farkas/got-hangman/blob/main/images/background.image.png)
2. Logo
Logo was created by ASCIIART.eu from an image of the Game of Thrones logo
![GoT Logo](https://github.com/tmea-farkas/got-hangman/blob/main/images/ascii.logo.png)
3. Favicon
The favicon was added to further elevate user satisfaction
![GoT Favicon]()
4. Colour coordinated messages
    - Green colour for positive reinforcement
![Green message](https://github.com/tmea-farkas/got-hangman/blob/main/images/green.message.png)
    - Red for failed input
![Red message](https://github.com/tmea-farkas/got-hangman/blob/main/images/red%20message.png)
5. Y/N choice questions
For easy navigation Yes or No questions were implemented where appropriate to ensure the user of a good flow of navigation through the game
![Y/N questions](https://github.com/tmea-farkas/got-hangman/blob/main/images/question1.png)
6. Input validation
Input validation has been implemented wherever user input was requested to avoid undesired input being accepted therefore damaging user experience.
![Input validation](https://github.com/tmea-farkas/got-hangman/blob/main/images/validation.png)

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
To deploy the project I followed the steps provided by C.I at the end of the Love Sandwiches walkthrough project:
- first I cleaned up the run.py file
- added import files to the requirements.txt
- on to Heroku where I created a new app
    - adding the name and region
    - added relevant config vars in the Settings section
    - added Python and NodeJS buildpacks
    - connected to GitHub in the Deploy section
    - searched for the repository
    - enabled automatic deploys so Heroku would deploy the project every time there was a new push to GitHub


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
- favicon not displaying
    - changed the file paths 

# Credits

Code written by me with the help of:

- Matthew Bodden - my mentor
- Slack colleagues
- Youtube tutorials - ex.: https://www.youtube.com/watch?v=m4nEnsavl6w&t=173s

Thank you!

