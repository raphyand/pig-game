#!/usr/bin/env python3


#Should have classes: 
#   Dice
#   Game Manager
#   Player
#       Computer
#   Score Board
#   Display Manager

from utils import AIBehaviors, gameState
from GameManager import GameManager
from DisplayManager import DisplayManager
from Player import Player, Computer

def main():

    #Instantiate Objects for Pig
    myGameManager = GameManager(0,0)
    #myGameManager.rollDice()
    #player1 = Player("Raphy", 0,0,0, False)
    #player2 = Computer("Henry the Robot", 0,0,0, True, AIBehaviors.NEUTRAL)
    #myGameManager.mainMenu()
    #player3 = Computer("Alexa the Despacito", 0, 0, 0, True, AIBehaviors.NEUTRAL)
    #myGameManager.turnMenu(player3)
    
    #Main Gameplay Loop
    while myGameManager.getCurrentGameState() is not gameState.GAMEOVER:

        if (myGameManager.getCurrentGameState() is gameState.MAIN_MENU):
            myGameManager.mainMenu()
        elif(myGameManager.getCurrentGameState() is gameState.PLAYER_SELECTION_MENU):
            myGameManager.playerSelectionMenu()
        elif(myGameManager.getCurrentGameState() is gameState.WHO_GOES_FIRST):
            myGameManager.whoGoesFirst_Menu()
        elif(myGameManager.getCurrentGameState() is gameState.TURN_MENU):
            myGameManager.turnMenu(myGameManager.getCurrentPlayer())


if __name__ == "__main__":
    # execute only if run as a script
    main()

