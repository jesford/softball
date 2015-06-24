## Softball Coaching

This python code allows me to randomly select players to sit each
inning, and assigns the fielders to positions based on their fielding
preferences.

**coach.py** has been revamped to include a Team() class. Your team is
now an object that you can add/remove players from, and assign
positions for. Example usage is given below...

#### How to coach a softball game without doing too much thinking.

#### OR Less thinking, more hitting.

*For now, open an ipython session, and do:*

from coach import *

*Create a Team object*

demons = Team()

*To get set up for the game, import regulars and add players as required*

demons.regulars()
demons.add()  #repeat as necessary

*If someone leaves early, or a regular doesn't show, remove them*

demons.remove()

*Each time a new inning starts, run*

demons.inning()

*which will print out a random selection of sitting and fielding players for each position. If no one could be matched to a position, the program will suggest a volunteer.*
