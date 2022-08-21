# ChessTour
### Project 4 Open Classrooms D-A Python
This project is a chess tournament manager made with Python3 and TinyDB.
## Installation:

Clone the repository:
```
git clone https://github.com/GrolschSec/ChessTour.git 
```  
Move into the project directory:
```
cd ChessTour
```  
Create a python virtual environment:
```
python3 -m venv env
```  
Activate the virtual environment (macOS, Linux):
```
source env/bin/activate  
```
Activate the virtual environment (Windows):
```
env\scripts\activate.bat
```
Install all the dependencies:
```
pip3 install -r requirements.txt
```

## Launch the program  
```
python3 main.py
```
Once you'll launch the program you'll have three options:  
1. Go to the player menu.
2. Go to the tournament menu.
3. Quit the program.


### 1. The player menu:  
This menu permit to execute all operations about the players.  
- Add a player.
- Modify a player.
- Remove a player.
- Show all players.

### 2. The tournament menu:
This menu permit to create a new tournament or continue, it also contains the report submenu.  
- Create a tournament.
- Continue a tournament.
- Report menu:
1. List all users by alphabet order or by classment.
2. List all tournaments
3. Once a tournament selected:
    1. Show the players of the tournament (alphabet or classment).
    2. Show the rounds, if you select a round you'll all the games of the round.  


## Generate a flake8 html report:
The configuration file for flake8 is named '.flake8' in the project dir.  
To generate the report just run the following command.  
```
flake8 --format=html --htmldir=flake-report
```
