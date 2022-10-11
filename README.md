# Battleship
Battleship is a strategy type guessing game for two players. It is played on ruled grids on which each player's fleet of warships is marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
In this version, each boat occupies a 1 per 1 square and the opponent is the computer. All its functions have been randomized using python.

<img src="images/responsive.png" alt="image of app on different sized screens">

[Click here to go to the live website!]

## Table of contents 
1. [User experience](#user-experience)
2. [Structure](structure)
4. [Features](#features)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## User experience

### Project Goals:

* The game provides a structure that is easy to understand, navigate and interact with.

* Contains fun colours and interactivity to engage the player in the game.

* Customisation of the size of the board and the number of ships.

* Incorporates a rules section that is easily accessible and understandable to the player.

* Player can play as many times as he wants without the need of refreshing

### Color scheme

* Blue ("\033[0;34m"): General text

* Red ("\033[0;31m"): Error, wrong input or loosing message

* Green ("\033[0;32m"): Winning messge and correct hit

* White ("\033[0;37m"): Board display and title


## Structure 

The game mechanics were conceived before starting to code. A flow chart was used for the process:

* Blue: Shows either an input from the user, a calculation made by the program or displays of information on the terminal

* Red: Validation of the input

* Green: The flow chart continues on the next green circle

Here we can see the game mechanics flowchart:
![Game mechanics flowchart image](assets/media/flow_chart.jpg)

## Features

Existing features:

* User selects the dificulty of the game:
    * Chooses the size of the board. Rows and columns are set independtly, no need for a square board. Sizes can be set between 3 and 6.

    * Chooses the number of ships. Limited to 8, since the smallest board permits has 9 locations.

* Enemy actions are randomized:

    * Placement of ships

    * Shooting the user

* User actions are made by him:

    * The location of his boats
    
    * Shooting the enemy

* User and enemy board:

    * @: marks the location a boat (Only for the user board).

    * *: marks an empty location (User board) or an unknown location (enemy board).

    * X (green): marks a boat that has been hit by the other player.

    * 0 (red): marks a location that has been shot with no boat.

* Other features:

    * Instructions section

    * Game can be repeated or ended at the end of each match up.

    * Input errors are shown in red

    * Teminal clears to avoid saturation of the console

    * Title of the game is always shown

    


