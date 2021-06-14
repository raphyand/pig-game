#!/usr/bin/env python3


#Should have classes: 
#   Dice
#   Game Manager
#   Player
#       Computer
#   Score Board
#   Display Manager

import dice
from GameManager import GameManager

def main():
    print("This is a test.  It should be printed out.")
    myGameManager = GameManager(0,0)
    myGameManager.rollDice()


if __name__ == "__main__":
    # execute only if run as a script
    main()

