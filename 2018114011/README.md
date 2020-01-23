# JETPACK-JOYRIDE - "Terminal-based version"

## **Coded by** :- *Ramaguru Guru Ravi Shanker - 2018114011*

## About :-
```
Jetpack Joyride is a 2011 side-scrolling endless runner action video game created by Halfbrick Studios. The game features the same protagonist from Monster Dash, Barry Steakfries, who the player controls as he steals a jet pack from a top-secret laboratory. The game has been met with very favorable reviews, and has won numerous awards. 
This is a terminal version of the 'Super Mario Bros' game. It exhibits Object-Oriented Programming concepts like encapsulation, inheritance, abstraction and polymorphism.
```
## Pre-requisites :-
```
In order to play this game, python3 should be installed install on your system and colorama module should be installed. Step to install are given for linux.
```
### Installation [For linux] :-
```
sudo apt-get update
sudo apt-get install python3
pip3 install colorama
```

## Instructions To Play 

* Run the following command to start the game.

    ```
	python3 game.py
    ```

* Use 'w' - to move up, 'a' - to move left and 'd' to move right to control player.

* Use 'e' to fire bullets.(which destroys the beams and also kills the boss)

* Use 'Space' to activate shield around player.(saves from beams)

* Hero is the main player of the game.

* Has 5 lives. If the case, Mandolian is respawned always at the current position  of him.

* Has 160 seconds to complete the game.

* Can fire bullets.

### Scenery

* background keeps changing

* It contains  obstacles, coins

### Coins
* Comes randomly at any point 

* Player score increases on collecting it(5)

### Beams

* There are three types of beams :-
1) Horizontal beam
2) Vertical beam
3) Diagonal beam

* comes randomly at any point

* Mandolian loses a life on colliding with a beam

* Can be destroyed by a bullet fired by Mandolian
* Saved by shield

#### Magnet

* Comes randomly at any point

* Constantly attracts Mandolian towards it if it is in certain range (in x direction)

* Can't be destroyed

### Boss_enemy

* Comes at end of the game

* Continuosly throws ice balls at Mandolian every 5 sec

* If hit Life of mandalorian decreases

* Defeated by shooting 3 bullets at Boss

* Adjust its position in accordance with Mandolian's y-coordinate

* Killed by one bullet, game is over


### Shield

* Used to shield Mandolian from obstacles

* refills at every 60 seconds

* Once occupied, it lasts for 10 seconds

* If Mandolian collides with obstacle it saves Mandolian

* can be occupied by pressing 'Space' if shieldmode is True

* Mandolian gets # symbol when it is on

### Speed_booster

* Comes randomly at any point 

* Game speed increases on collecting it

* Once occupied, it lasts for 5 seconds

### Color 

* Different colors are given to different components of the game


### Score 

* Increases by collecting coins

* Increases by hitting beams by fire

* Increases by killing boss


