## Softball Coaching

This python script allows me to randomly select players to sit each inning, and assigns the fielders to positions based on their fielding preferences.

There are two functions in **coach.py**:

- **new_player()** adds a player to the roster. Each time it is run, it will ask for player name, and preferred fielding positions (which can be one, several, or all positions).

- **inning()** generates a new list of players on the bench and players assigned to each position. It attempts to put players in one of their preferred positions, but when this is not possible (maybe all the input left fielders were chosen to sit) it will suggest a volunteer.

#### How to coach a softball game without doing too much thinking.

#### OR Less thinking, more hitting.

*For now, just open an ipython session, and do:*

from coach import new_player, inning

*To get set up for the game, repeatedly run*

new_player()

*to add players to the roster. Each time a new inning starts, run*

inning()

*which will print out a random selection of sitting and fielding players for each position. If no one could be matched to a position, the program will suggest a volunteer.*
