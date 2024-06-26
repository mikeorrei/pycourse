# PyCourse Documentation
Repository for all of the code being resented during the class.

# Class Schedule
## Week 1 - 3/8
Topics Covered:
- Introduction of Python
- Variables
- Data Structures
- Conditionals
- Loops

Assignment:

Two provided dictionaries for monsters and player attacks  
They can be tweaked, re-named, whatever  
Dictionaries can be found below:  
- /week_one/homework.py

Basic flow of the game is as follows:
- Monster gets randomly selected and introduced to the player
- Display monster's name and health
- Prompt user for attack choice
- Show damage done to the monster
- Monster damages the player with a random attack
- When either the monster or player's health is zero battle ends
- Up to you what happens next
  - Player can have the option to continue or quit
  - New monster can be selected with no player input

## Week 2 - 3/22
Topics Covered:
- Function basics
- Importing packages

Assignment:
Start by converting last week's homework into functions wherever possible
Try to keep them small, it's generally better to have more small functions
Anything that repeats is high priority for a function

After that, if you want, you can implement item drops from monsters
I would recommend ignoring the strength and hast items to start with
Beyond that you can add the skip and cooldown to player attacks
Skip will skip X player turns
Cooldown means it can't be used again for X turns

The starting code can be found in week_two/homework.py

## Week 3 - 4/5
Topics Covered:
- Continued Functions Discussion
- Tokenization and Parsing
- Abstract Syntax Trees
- Recursion

Assignment:
Continue with assignment from week 2
Feel free to expand the game as much as you'd like

## Week 4 - 4/19
Topics Covered:
- Classes
- Inheritance
- Methods

Assignment:
Work on converting the previous assignment into classes
Feel free to create as many or as little as you like
You can use the Player and Character classes I built during class
If you use my classes they will most likely need to be adjusted to fit your game

Other class ideas:
- Monster class
- Item class
- Sub Item class (Healing Items, Buff Items, etc)
- Make the game itself a class
