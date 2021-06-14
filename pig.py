#!/usr/bin/env python3


#Should have classes: 
#   Dice
#   Game Manager
#   Player
#       Computer
#   Score Board
#   Display Manager

from utils import AIBehaviors
from GameManager import GameManager
from Player import Player, Computer

def main():
    print("This is a test.  It should be printed out.")
    myGameManager = GameManager(0,0)
    myGameManager.rollDice()
    player1 = Player("Raphy", 0,0,0, False)
    player2 = Computer("Henry the Robot", 0,0,0, True, AIBehaviors.NEUTRAL)
    player1.printPlayerSheet()
    print("")

    player2.printPlayerSheet()
if __name__ == "__main__":
    # execute only if run as a script
    main()

