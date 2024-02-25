Welcome to the Game of Thrones Hangman!

![Game window](https://github.com/tmea-farkas/got-hangman/blob/main/images/game.page.png)
[Game of Thrones Hangman](https://got-hangman-46eee30c0ce3.herokuapp.com/)

# The project
This project is a classic Hangman game with a theme applied from the popular TV Show Game of Thrones. This is represented by not only the logo, but the guessable character names and wording of the game creating the illusion of a quest for the player, essentially involving them in the story.


## UXD (User Experience Design)
- **The Strategy Plane**
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

### **The Scope Plane**
At this stage I used the previously gathered knowledge to create a basic idea of what features to implement for the user and what steps to take achieving those goals.
    - e.g. 
        - asking for user name
        - implementing the user name into the rules to make it more personalised
        - writing up the character names that are to be guessed
        - creating a story behind the game to make it more enjoyable and engaging increasing the chance for return visits
        - making sure print statements are worded to fit to the theme

### **The Structure Plane**

*Images*:
Considering images that are both within the theme and aestethically pleasing not losing sight of accessibility and ux.

*Colours*:
The use of a basic colour-scheme meant that the project will not look too crowded, providing ease while staying within the "bloody" theme of Game of Thrones.

### **The Skeleton Plane**
The Skeleton plane contributes to the placement of visual media and texts for maximum effect and efficiency. Where the structure plane begins to give shape to the mass of requirements arising from our strategic objectives the skeleton plane further refines that structure, identifying specific aspects of interface, navigation, and information design that will make the intangible structure concrete.

### **The Surface Plane**
The last stage of development, where decisions are finalised and implemented with concerns to the users sensory experience. Making the game including the colour palette and layout, where the logo appears, important information, user input requests, colour-coding to draw the users attention to key information.

1. **Favicon**

The favicon was added to further elevate user satisfaction by providing an icon within the theme that is easily recognisable and visible.

![GoT Favicon](https://github.com/tmea-farkas/got-hangman/blob/main/images/favicon.png)

2. **The velcome page**

Upon loading the page the user is provided with the game terminal that has the theme-logo, a welcome message and user input request to provide a name for the user. Further more the page has a background image added to it to further boost the experience, creating the illusion that the user is the knight on the image that has to fight the dragon (the game itself). The logo was created by ACSIIART.eu from an image of the Game of Thrones logo.
The name input has a validation rule that only allows the user to input a name that is less than 10 characters long and is only letters.

![background image](https://github.com/tmea-farkas/got-hangman/blob/main/images/background.image.png)

![welcome page](https://github.com/tmea-farkas/got-hangman/blob/main/images/welcome.png)

![Name validation](https://github.com/tmea-farkas/got-hangman/blob/main/images/name.validation.png)

3. **Rules Display**

Once the user has provided their name the next step in the game is that the rules are displayed in the terminal, incorporating the name provided within.  
At the end of the rules the user is asked if they are ready to start the game or not. If the user input is "Y" the game starts, if "N" the user will be taken back to the welcome page; if any other input then the user will be prompted to provide a valid input.

![Game rules](https://github.com/tmea-farkas/got-hangman/blob/main/images/rules.png)

![Game start validation](https://github.com/tmea-farkas/got-hangman/blob/main/images/validation1.png)

5. **The Game**

Once the user starts the game, is provided with the "gallows" that will be appended with each failed guess. The user also has the number of guesses displayed as well as a display of the letters guessed so far and a request to guess a letter.

![Game start](https://github.com/tmea-farkas/got-hangman/blob/main/images/start.game.png)

- The number of tries will decrease with each failed guess, while each guessed letter will be added to the relevant display message.
- Once the game started the user will be provided with instant feedback messages that will confirm correct/incorrect guesses using colour-coded messaging.

![Positive guess](https://github.com/tmea-farkas/got-hangman/blob/main/images/stages1.png)

![Negative guess](https://github.com/tmea-farkas/got-hangman/blob/main/images/stages2.png)


- The user will only be able to guess letters, otherwise a validation message will appear

![Letter input](https://github.com/tmea-farkas/got-hangman/blob/main/images/letter.validation.png)

6. **Input validation**
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
## Forking and Cloning
- The following steps are to be taken to fork a repository:
    - go to repository
    - click on the downward arrow next to Fork
    - click "Create a new fork"
    - name your repository
    - click "create fork"
This will create a copy of the original repository in a remote location.
- to Clone a repository:
    - click on "Code"
    - copy repository URL
    - open your IDE
    - click on clone repository
    - copy the url
This will create a local copy of the repository.



# Testing
The project has gone through continuous testing during development using print messages at every stage. Has been tested by several users.
It has also been tested by pep8 standards which provided no issues with the code.

## Manual Testing
|        Feature    Expectation           |     Testing                   |        Result             |      Pass/Fail  |
|               :--------:                |     :-----:                   |       :--------:          |      :----:     |
|Background image display on page load    | Loading game window           |Image displaying           |         ✔       |
|Logo to appear on page load              | Loading game window           |Logo appears               |         ✔       |
|Welcome message to display on page load  | Loading game window           |Message displaying         |         ✔       |
|Ask user for name input on load          | Loading game window           |Input request displaying   |         ✔       |
|Input validation  (< 10 characters & alphabetical) message to appear until a valid input is provided | Typing more than 10 characters|Validation message appears |         ✔       |
|Rules Displayed  | Name input completion + Enter |Displaying rules  |         ✔       |
|Y/N choice to take user to game or back to logo display| Name input completion + Enter |- if Y = go to game, - if N = go to logo, if else = display error message and ask again |         ✔       |
|Display hangman stages w/ each guess     |Game entry choice answer = Y and game is baing played  |Displaying each stage      |         ✔       |
|Keep track of guessed letters with a print statement and add each guessed letter| Letter inputs  |Letters displaying         |         ✔       |
|Display error(red) message when letter is not in the word  | Wrong letter input            |Message displaying and promts user until correct input |         ✔       |
|Display confirmation(green) message when letter is in the word| Correct letter input          |Message displaying and prompts user until correct input |         ✔       |
|Reveal result if not guessed within available number of tries | Incorrect guess until out of tries |Message displaying |         ✔       | 
|Reveal confirmation message when name guessed correctly before tries run out | Correctly guessing before tries run out   |Message displaying |         ✔       |
|Y/N question to play another game  | Finishing the game   |- if Y = new game, - if N = back to logo, if else = prompt user to correct input |         ✔       |


# Bugs
- clearing the window at the wrong line
    - moved the clear_window() function call to the relevant places
- indentation issue with print statements
    - fixed by adjusting the indentation
- not taking the user back to the top at the end of the game
    - called the relevant function at the end
- favicon not displaying
    - changed the file paths 

# Acknowledgements

Code written by me with the help of:

- Matthew Bodden - mentor
- Slack colleagues
- Youtube tutorials - ex.: https://www.youtube.com/watch?v=m4nEnsavl6w&t=173s

Thank you!

