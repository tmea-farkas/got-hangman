Welcome to the Game of Thrones Hangman!

![Game window](https://github.com/tmea-farkas/got-hangman/blob/main/images/hangman.png)
[Game of Thrones Hangman](https://got-hangman-46eee30c0ce3.herokuapp.com/)

# The project
This project is a classic Hangman game with a theme applied from the popular TV Show Game of Thrones. This is represented by not only the logo, but the guessable character names and wording of the game creating the illusion of a quest for the player, essentially involving them in the story.


## UXD (User Experience Design)
- The Strategy Plane
This first stage of development consists of doing the research on what will be the use of the project. Finding out what the user would like to see in the project and what they want to use it for.

*First-Time user goals*
- accessing information relating to the game
- undestanding the flow of the game and rules
- navigate the game through without having to reload the page
- be able to play the game again
- access to a score board

*Returning user goals*
- be able to use the game again with ease
- to have access to a top10 score board

*Developer goals*
- to provide a game for Game of Thrones fans
- to ensure easy navigation
- to use media elements enhancing user experience
- to make a game that is engaging and entartaining to both first-time and returning users

- The Scope Plane
At this stage I used the previously gathered knowledge to create a basic idea of what features to implement for the user and what steps to take achieving those goals.
    - e.g. 
        - asking for user name
        - implementing the user name into the rules to make it more personalised
        - writing up the character names that are to be guessed
        - creating a story behind the game to make it more enjoyable and engaging increasing the chance for return visits
        - making sure print statements are worded to fit to the theme

- The Structure Plane

*Images*
Considering images that are both within the theme and aestethically pleasing not losing sight of accessibility and ux.

*Colours*
The use of a basic colour-scheme meant that the project will not look too crowded, providing ease while staying within the "bloody" theme of Game of Thrones.

- The Skeleton Plane
The Skeleton plane contributes to the placement of visual media and texts for maximum effect and efficiency. Where the structure plane begins to give shape to the mass of requirements arising from our strategic objectives the skeleton plane further refines that structure, identifying specific aspects of interface, navigation, and information design that will make the intangible structure concrete.

- The Surface Plane
The last stage of development, where decisions are finalised and implemented with concerns to the users sensory experience. Making the game including the colour palette and layout, where the logo appears, important information, user input requests, colour-coding to draw the users attention to key information.

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
## Forking


# Testing
The project has gone through continuous testing during development using print messages at every stage. Has been tested by several users.
It has also been tested by pep8 standards which provided no issues with the code.

## Manual Testing
|        Feature    Expectation           |        Testing           |      Results  |
|               :--------:                |       :--------:         |      :----:   |
|Background image display on page load    |Image displaying          |         ✔     |
|Logo to appear on lage load              |Logo appears              |         ✔     |
|Welcome message to display on page load  |Message displaying        |         ✔     |
|Ask user for name input                  |Input request displaying  |         ✔     |
|Validation  (< 15 characters )           |validation message        |         ✔     |
|Rules Displayed                          |Displaying                |         ✔     |
|Y/N choice to take user to game or back  |if Y = go to game         |         ✔     |
|      to logo display                    |if N = go to logo         |         ✔     |
|Display hangman stages w/ each guess     |Displaying next stage     |         ✔     |
|Keep track of guessed letters            |Letters displaying        |         ✔     |
|Display error(red)message when letter    |Message displaying        |         ✔     |
|is not in the word                       |                          |         ✔     |
|Display confirmation message(green) when |Message displaying        |         ✔     |
|letter is in the word                    |                          |         ✔     |
|Reveal result if not guessed with        |Message displaying        |         ✔     | 
|relevant message                         |                          |         ✔     |
|Reveal confirmation message when name    |Messag displaying         |         ✔     |
|guessed correctly before tries run out   |                          |         ✔     |
|Y/N question to play another game or not |Y = new game              |         ✔     |
|                                         |N = back to logo          |         ✔     |


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

