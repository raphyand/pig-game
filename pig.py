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
from DisplayManager import DisplayManager
from Player import Player, Computer

def main():

    game_is_not_over = False
    

    myGameManager = GameManager(0,0)
    #myGameManager.rollDice()
    player1 = Player("Raphy", 0,0,0, False)
    player2 = Computer("Henry the Robot", 0,0,0, True, AIBehaviors.NEUTRAL)
    #myGameManager.mainMenu()
    player3 = Computer("Alexa the Despacito", 0, 0, 0, True, AIBehaviors.NEUTRAL)
    myGameManager.turnMenu(player3)

if __name__ == "__main__":
    # execute only if run as a script
    main()

